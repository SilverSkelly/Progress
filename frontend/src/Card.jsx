import { Link } from 'react-router-dom';
import React from 'react'


function Card (props) {


    return(
        <>
        
        <div className = "card">         
            <img className= "card-image" src="https://via.placeholder.com/100" alt="Anime Theme Card"/>
            <h3><Link to= "/" >{props.name}</Link></h3>
        </div>
        </>
    );
}


export default Card;