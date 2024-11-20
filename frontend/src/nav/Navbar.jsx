import React from 'react'
import './Navbar.css'


function Navbar() {
  return (
    <header className="header">
        <a href="/" classname="logo">Progress</a>
        <nav className="navbar">
            <a href="/">Build</a>
            <a href="/">Search</a>
        </nav>
    </header>
  )
}

export default Navbar