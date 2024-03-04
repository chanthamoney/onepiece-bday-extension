# Welcome to the One Piece Birthday Extension

This is Google Chrome extension is made by Shalinikantcode and Chanthamoney. They were inspired one day while working and seeing a calendar that displayed Animal Crossing character's Birthday. This extension scrapes the One Piece fandom wiki for characters birthdays, name, and portraits and writes it to a json file. The extension reads the json file and shows the character whose birthday matches the current date.

## How to run the scraping script
We used jupyter notebook and beautiful soup to run the python script. You can download the file and then run the command
>  jupyter notebook

## How to download the extension
- Clone this repo
- Go to chrome's extension page
- Enable Developer mode
- Click on `Load unpacked`
- Select the one piece build directory

You're done! Click on the straw hat and you should see who's birthday it is today! 

## Updating the build
If you added anything to this repo and want to see the changes you can
- run the command `yarn run build`
- Go to chrome's extension page
- Click on `Load unpacked` and select the `my-app` build folder. NOT the `one piece build` folder


