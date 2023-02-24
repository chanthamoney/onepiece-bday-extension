import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { onePieceData } from "../src/data/one_piece_character_data";
import { onePieceCharacterType } from "../src/types/types";
import BirthdayCard from "./BirthdayCard";

function App() {
  const date = new Date();
  let day = date.getDate().toString();
  let month = date.getMonth() + 1;
  console.log(date);

  const birthdays = onePieceData.filter(
    (charaObject: onePieceCharacterType) =>
      charaObject.birth_month === month && charaObject.birth_day === day
  );

  console.log("birthdays", birthdays);

  return (
    <div className="App">
      <BirthdayCard character={birthdays[0]}></BirthdayCard>
    </div>
  );
}

export default App;
