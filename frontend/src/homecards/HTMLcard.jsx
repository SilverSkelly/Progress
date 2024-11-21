import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'HTML' category card on the homepage, linking to its vocab ///

function HTMLcard() {
  return (
    <>
    <Link to="/html">
        <div className="newcard">
          <img src="src/assets/html.jpg" />
        </div>
      </Link>
        
      
    </>
  );
}

export default HTMLcard;
