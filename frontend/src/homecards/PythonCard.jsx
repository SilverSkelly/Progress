import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'Python' category card on the homepage, linking to its vocab ///

function PythonCard() {
  return (
    <>
      <Link to="/python">
        <div className="newcard">
          <img src="src/assets/python.jpg" />
        </div>
      </Link>
    </>
  );
}

export default PythonCard;