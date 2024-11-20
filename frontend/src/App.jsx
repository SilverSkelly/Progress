import { useState } from "react";
import Card from "./Card.jsx";
import "./App.jsx";
import "./index.css";
import Navbar from "./nav/navbar.jsx";
import FundamentalsCard from "./homecards/FundamentalsCard.jsx";
import Fundamentals from "./pages/Fundamentals";
import HTMLcard from "./homecards/HTMLcard.jsx";
import CSScard from "./homecards/CSScard.jsx";
import JavascriptCard from "./homecards/JavascriptCard.jsx";
import PythonCard from "./homecards/PythonCard.jsx";
 


function App() {
  return (
    <>
    <Navbar/>
      <body>
        <div className="hero">
          <div className="welcome">Welcome to Progress!</div>
          <h2>
            Get ready for a coding adventure! Explore different programming
            languages with anime-inspired lessons and take your skills to the
            next level.
          </h2>
        </div>
        <br />
        <FundamentalsCard />
        <HTMLcard />
        <CSScard />
        <JavascriptCard />
        <PythonCard/>
      </body>
    </>
  );
}

export default App;
