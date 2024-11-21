import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom';
import Syntax from '../vocabulary_cards/Fundamentals_vocab.jsx/syntax';
import Navbar from '../Navbar/Navbar';
import Data from '../vocabulary_cards/Fundamentals_vocab.jsx/Data';
import Variable from '../vocabulary_cards/Fundamentals_vocab.jsx/Variable';
import Datatype from '../vocabulary_cards/Fundamentals_vocab.jsx/Datatype';
import Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Operators';
import Assignment_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Assignment_O';
import Arithmetic_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Arithmetic_O';
import Relational_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Relational_O';
import Logical_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Logical_O';
import Bitwise_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Bitwise_O';
import Conditional_Operators from '../vocabulary_cards/Fundamentals_vocab.jsx/Conditional_O';
import State from '../vocabulary_cards/Fundamentals_vocab.jsx/State';
import Integer from '../vocabulary_cards/Fundamentals_vocab.jsx/Integer';
import String from '../vocabulary_cards/Fundamentals_vocab.jsx/String';
import Function from '../vocabulary_cards/Fundamentals_vocab.jsx/Function';

function Fundamentals() {
  return (
<div >
  <Navbar/>
    <div className="fundamentalsbg">
      <h1 className="whiteword">Fundamentals Vocab</h1>
    <Syntax/>
    <Data/>
    <Variable/>
    <Datatype/>
    <Operators/>
    <Assignment_Operators/>
    <Arithmetic_Operators/>
    <Relational_Operators/>
    <Logical_Operators/>
    <Bitwise_Operators/>
    <Conditional_Operators/>
    <State/>
    <Integer/>
    <String/>
    <Function/>
    </div></div>
  )
}

export default Fundamentals