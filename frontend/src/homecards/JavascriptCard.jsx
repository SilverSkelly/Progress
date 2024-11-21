import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'Javascript' category card on the homepage, linking to its vocab ///

function JavascriptCard() {
  return (
    <>
      <Link to="/javascript">
        <div className="newcard">
          <img src="src/assets/js.jpg" />
        </div>
      </Link>
    </>
  );
}

export default JavascriptCard;
