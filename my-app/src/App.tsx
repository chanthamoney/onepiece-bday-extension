import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { onePieceData } from "../src/data/one_piece_character_data";
import { onePieceCharacterType } from "../src/types/types";

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
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React shalini
        </a>
      </header>
    </div>
  );
}

export default App;
