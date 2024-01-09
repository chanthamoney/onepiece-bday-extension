import "./App.css";
import { onePieceData } from "../src/data/one_piece_character_data";
import { onePieceCharacterType } from "../src/types/types";
import BirthdayCard from "./BirthdayCard";
import Carousel from "react-material-ui-carousel";

function App() {
  const date = new Date();
  let day = date.getDate();
  let month = date.getMonth() + 1;
  console.log(date);

  const birthdays = onePieceData.filter(
    (charaObject: onePieceCharacterType) =>
      charaObject.birth_month === month && charaObject.birth_day === day
  );

  return (
    <div className="App">
      <Carousel navButtonsAlwaysVisible autoPlay={false} height={"500px"}>
        {birthdays.map((birthday, i) => {
          return <BirthdayCard character={birthday} key={i}/>;
        })}
      </Carousel>
    </div>
  );
}

export default App;
