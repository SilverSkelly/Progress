import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'HTML' category card on the homepage, linking to its vocab ///

function HTMLcard() {
  return (
    <>
      <div className="card">
        <img
          className="card-image"
          src="https://via.placeholder.com/100"
          alt="Anime Theme Card"
        />
        <h3>
          <Link to="/html">HTML</Link>
        </h3>
      </div>
    </>
  );
}

export default HTMLcard;
