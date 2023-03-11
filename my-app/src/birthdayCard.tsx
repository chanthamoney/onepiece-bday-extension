import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import CakeIcon from "@mui/icons-material/Cake";

interface birthdayCardProps {
  character: {
    name: string;
    birthday: string;
    img_url: string;
  };
}
export default function BirthdayCard({ character }: birthdayCardProps) {
  const { birthday, name, img_url } = character;
  const regexp = /.+.png/gm;
  const regexArray = regexp.exec(img_url);
  const image = regexArray?.[0];
  console.log(regexArray);
  return (
    <Card sx={{ maxWidth: 500, height: 500 }}>
      <img crossOrigin="anonymous" referrerPolicy="no-referrer" src={img_url} />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {birthday}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">
          <CakeIcon />
        </Button>
      </CardActions>
    </Card>
  );
}
