import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom';
import Vocabword3 from '../vocabulary_cards/Javascript_vocab.jsx/Vocabword3';
import Navbar from '../Navbar/Navbar';

function Javascript() {
  return (
<div>
    <Navbar/>
    <div><h1 className="categorytitle">JavaScript Vocab</h1></div>
    <Vocabword3/>
    </div>
  )
}

export default Javascript