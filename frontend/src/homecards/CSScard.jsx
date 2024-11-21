import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'CSS' category card on the homepage, linking to its vocab ///

function CSScard() {
  return (
    <>
      <Link to="/css">
        <div className="newcard" >
          <img src="src/assets/css.jpg" />
        </div>
      </Link>
    </>
  );
}

export default CSScard;
