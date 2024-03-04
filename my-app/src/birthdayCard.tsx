import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import CakeIcon from "@mui/icons-material/Cake";
import { Link } from "@mui/material";

interface birthdayCardProps {
  character: {
    name: string;
    birthday: string;
    img_url: string;
    wiki_url: string;
  };
}
export default function BirthdayCard({ character }: birthdayCardProps) {
  const { birthday, name, img_url, wiki_url } = character;
  const regexp = /.+.png/gm;
  const regexArray = regexp.exec(img_url);
  const image = regexArray?.[0];
  return (
    <Card sx={{ maxWidth: 500, height: 400 }}>
      <img src={img_url} height="250px" width="250px" />
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
        <Link href={wiki_url}>WIKI</Link>
      </CardActions>
    </Card>
  );
}
