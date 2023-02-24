import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { onePieceCharacterType } from "../src/types/types";

interface birthdayCardProps {
    character : {
        name: string,
        birthday: string,
        img_url: string
    }
}
export default function BirthdayCard({character} : birthdayCardProps) {
    const {birthday,name,img_url} = character
    const regexp = /.+.png/gm
    const regexArray = regexp.exec(img_url)
    const image = regexArray?.[0]
    console.log(regexArray)
  return (
    <Card sx={{ maxWidth: 1000 }}>
      <CardMedia
        component="img"
        alt="green iguana"
        height={500}
        image={image}
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {birthday}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Share</Button>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}
