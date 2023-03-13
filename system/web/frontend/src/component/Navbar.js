import React, { useState, useEffect } from 'react';
import '../component/Navbar.css';

function Navbar() {
  const [click, setClick] = useState(false);

  //const handleClick = () => setClick(!click);
  const closeMobileMenu = () => {
    setClick(false);
  };


  return (
    <>
      <nav className='navbar'>
        <div className='navbar-container'>
          <a href='http://localhost:3000/' className='navbar-logo' onClick={closeMobileMenu}>
            HUST & NDT 
            <i class='fas fa-spa' />
          </a>

          <ul className={click ? 'nav-menu active' : 'nav-menu'}>
            <li className='nav-item'>
              <a href='http://localhost:3000/' className='nav-links' onClick={closeMobileMenu}>
                Home
              </a>
            </li>
            <li className='nav-item'>
              <a
                href='http://localhost:3000/services'
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Services
              </a>
            </li>
            <li className='nav-item'>
              <a
                href='http://localhost:3000/products'
                className='nav-links'
                onClick={() => closeMobileMenu}
              >
                Products
              </a>
            </li>
            <li className='nav-item'>
              <a
                href='http://localhost:3000/fluctuations'
                className='nav-links'
                onClick={closeMobileMenu}
              >
                Charts
              </a>
            </li>
          </ul>
          
        </div>
      </nav>
    </>
  );
}

export default Navbar;
