import React from 'react'
import { BrowserRouter, Link } from 'react-router-dom';
import './Navbar.css'

function Navbar() {
  return (
    <header className="header">
        <a href="/" className="logo">Progress</a>

        <nav className="navbar">
            <a href="/">Build</a>
            <a href="/">Search</a>
        </nav>
    </header>
  )
}

export default Navbar