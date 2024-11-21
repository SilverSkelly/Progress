import React from "react";
import { BrowserRouter, Link } from "react-router-dom";

///this is the 'Fundamentals' category card on the homepage, linking to its vocab ///

function FundamentalsCard() {
  return (
    <>
      <Link to="/fundamentals">
        <div className="newcard">
          <img src="src/assets/Fundamentals3.jpg" />
        </div>
      </Link>
    </>
  );
}

export default FundamentalsCard;
