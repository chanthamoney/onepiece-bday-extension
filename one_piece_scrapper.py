#imports
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import json
from joblib import Parallel, delayed
import requests


characters_page = requests.get("https://onepiece.fandom.com/wiki/List_of_Canon_Characters")
characters_page.content

soup = BeautifulSoup(characters_page.content, 'html.parser')
print(soup.prettify())

# SLOW VERSION
def getCharacterUrl(name):
    baseUrl = 'https://onepiece.fandom.com/wiki/'
    #check if name has spaces
    if (' ' in name):
        name = name.replace(' ', '_')
    newUrl = baseUrl + name
    return newUrl

def getCharacterInfo(url, name):
    # case sensitive regex match on month and 1-2 digit date
    bday_regex = "(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})"
    character_page = requests.get(url)
    soup = BeautifulSoup(character_page.content, 'html.parser')
    sideBar = soup.find('aside')
    # only care about characters with birthdays
    if sideBar.find(attrs={"data-source": "birth"}):
        #birthday
        input_tag = sideBar.find(attrs={"data-source": "birth"})
        birthday_string = input_tag.find('div').contents[0]
        #birthday to month and day ints
        results = re.search(bday_regex, birthday_string)
        birth_day = int(results.group(2))
        birth_month = datetime.strptime(results.group(1), "%B").month
        # img url
        img = sideBar.find('img')['src']
        json_val = {'name': name, 'birthday': birthday_string, 'birth_month': birth_month ,'birth_day': birth_day, 'img_url': img }
        return json_val

# # SLOW VERSION
# # assumes first 2 tables are characters and the third is groups
# tables = soup.find_all('table', limit=2);
# json_array = []
# for table in tables:
#     rows = table.find_all('tr')
#     #need to skip the row in thead
#     print(len(rows), " characters to go")
#     for i, row in enumerate(rows):
#         if i > 0:
#             tds = row.find_all('td')
#             name = tds[1].text.strip()
#             url = getCharacterUrl(name)
#             val = getCharacterInfo(url, name)
#             if (val is not None):
#                 json_array.append(val)
#             if i%25==0:
#                 print(i," characters done")
# print(json_array)

#testing out "fast version" with parallel processing

def processRow(row):
    tds = row.find_all('td')
    name = tds[1].text.strip()
    return getCharacterUrl(name)

tables = soup.find_all('table', limit=2);
json_array = []
all_rows = []
for table in tables:
    #need to skip the first row - thead
    new_rows = table.find_all('tr')
    del new_rows[0]
    all_rows = all_rows + new_rows
    
print(len(all_rows), " characters to go")
url_list = [processRow(row) for row in all_rows]

def getCharacterPage(url):
    return {"url": url, "page": requests.get(url)}

print("processing char pages")
all_character_pages = Parallel(n_jobs=10)(delayed(getCharacterPage)(url) for url in url_list)

print("done with pages")


def getCharacterInfoFromPage(page,url):
    # case sensitive regex match on month and 1-2 digit date
    bday_regex = "(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})"
    soup = BeautifulSoup(page.content, 'html.parser')
    sideBar = soup.find('aside')
    # only care about characters with birthdays
    if sideBar.find(attrs={"data-source": "birth"}):
        # have to rebuild name due to parallel processing
        name = sideBar.find(attrs={"data-source": "name"}).text
        #birthday
        input_tag = sideBar.find(attrs={"data-source": "birth"})
        birthday_string = input_tag.find('div').contents[0]
        #birthday to month and day ints
        results = re.search(bday_regex, birthday_string)
        birth_day = int(results.group(2))
        birth_month = datetime.strptime(results.group(1), "%B").month
        # img url
        img = sideBar.find('img')['src']
        json_val = {'name': name, 'birthday': birthday_string, 'birth_month': birth_month ,'birth_day': birth_day, 'img_url': img , 'wiki_url': url}
        return json_val
 
def toJson(char_page):
    return getCharacterInfoFromPage(char_page["page"],char_page["url"])

print("start")
    
#iterative
json_array = [toJson(page) for page in all_character_pages]
#parallel
#json_array = Parallel(n_jobs=10)(delayed(toJson)(page) for page in all_character_pages)
        
print("done with json")

#removing nulls
json_array = list(filter(lambda item: item is not None, json_array))

# Serializing json
json_object = json.dumps(json_array, indent=4)
print(json_object)

# Writing to sample.json
with open("one_piece_character_data.json", "w") as outfile:
    outfile.write(json_object)

def remove_text_after_portrait(url):
    # Find the index of "Portrait.png"
    index = url.find("Portrait.png")
    
    # If "Portrait.png" is found, truncate the string up to that point
    if index != -1:
        new_url = url[:index + len("Portrait.png")]
        return new_url
    else:
        # If "Portrait.png" is not found, return the original URL
        return url

# Opening JSON file
f = open('one_piece_character_data.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)


# Iterating through the json
# list
# for i in range(0, 1):
# #     character_portrait_url = 'https://onepiece.fandom.com/wiki/Category:Character_Portraits'
#     name = data[i]['name']
#     test = requests.get('https://onepiece.fandom.com/wiki/Category:Character_Portraits?from=A')
#     soup = BeautifulSoup(test.content, 'html.parser')
#     img = soup.find('img', attrs={"alt": name+' Portrait.png'})['src']
#     # print(soup.prettify())
#     # img = soup.find(name+'_Portrait.png')
#     print('test', img)
#     new_img = remove_text_after_portrait(img)
#     print(' girl ' , new_img)
#     data[i]['img_url'] = new_img
#     print(data[i]['img_url'])

# How to loop through all json
for i in range(len(data) - 1, -1, -1):
    print('i : ', i)
    chara_portrait_url = 'https://onepiece.fandom.com/wiki/Category:Character_Portraits?from='
    name = data[i]['name']
    if name[0] == 'A':
        chara_portrait_url += 'A'
    elif name[0] == 'B':
        chara_portrait_url += 'B'
    elif name[0] == 'C':
        chara_portrait_url += 'C'
    elif name[0] == 'D':
        chara_portrait_url += 'D'
    elif name[0] == 'E':
        chara_portrait_url += 'E'
    elif name[0] == 'F':
        chara_portrait_url += 'F'
    elif name[0] == 'G':
        chara_portrait_url += 'G'
    elif name[0] == 'H':
        chara_portrait_url += 'H'
    elif name[0] == 'I':
        chara_portrait_url += 'I'
    elif name[0] == 'J':
        chara_portrait_url += 'J'
    elif name[0] == 'K':
        chara_portrait_url += 'K'
    elif name[0] == 'L':
        chara_portrait_url += 'L'
    elif name[0] == 'M':
        chara_portrait_url += 'M'
    elif name[0] == 'N':
        chara_portrait_url += 'N'
    elif name[0] == 'O':
        chara_portrait_url += 'O'
    elif name[0] == 'P':
        chara_portrait_url += 'P'
    elif name[0] == 'Q':
        chara_portrait_url += 'Q'
    elif name[0] == 'R':
        chara_portrait_url += 'R'
    elif name[0] == 'S':
        chara_portrait_url += 'S'
    elif name[0] == 'T':
        chara_portrait_url += 'T'
    elif name[0] == 'U':
        chara_portrait_url += 'U'
    elif name[0] == 'V':
        chara_portrait_url += 'V'
    elif name[0] == 'W':
        chara_portrait_url += 'W'
    elif name[0] == 'X':
        chara_portrait_url += 'X'
    elif name[0] == 'Y':
        chara_portrait_url += 'Y'
    else:
        chara_portrait_url += 'Z'
    print(chara_portrait_url)
    chara_page = requests.get(chara_portrait_url)
    soup = BeautifulSoup(chara_page.content, 'html.parser')
    img = soup.find('img', attrs={"alt": name+' Portrait.png'})
    if img is not None:
         new_img = remove_text_after_portrait(img['src'])
    else:
        ## delete this from json
        data.pop(i)
         # index_remove.append(i)
    print(' girl ' , new_img)
    data[i]['img_url'] = new_img

# Add new img url to a modified file 
newData = json.dumps(data, indent=4)
with open('modified.json', 'w') as file:
    # write
    file.write(newData)