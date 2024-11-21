import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom';
import Vocabword2 from '../vocabulary_cards/HTML_vocab.jsx/Vocabword2';
import Navbar from '../Navbar/Navbar';

function HTML() {
  return (
<div>
    <Navbar/>
    <div><h1 className="categorytitle">HTML Vocab</h1></div>
    <Vocabword2/>
    </div>
  )
}

export default HTML