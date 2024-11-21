import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom';
import Vocabword1 from '../vocabulary_cards/CSS_vocab.jsx/vocabword';
import Navbar from '../Navbar/Navbar';

function CSS() {
  return (
<div>
  <Navbar/>
    <div><h1 className="categorytitle">CSS Vocab</h1></div>
    <Vocabword1/>
    </div>
  )
}  




export default CSS