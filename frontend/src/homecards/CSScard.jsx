import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'CSS' category card on the homepage, linking to its vocab ///

function CSScard() {
  return (
    <>
      <div className="card">
        <img
          className="card-image"
          src="https://via.placeholder.com/100"
          alt="Anime Theme Card"
        />
        <h3>
          <Link to="/css">CSS</Link>
        </h3>
      </div>
    </>
  );
}

export default CSScard;
