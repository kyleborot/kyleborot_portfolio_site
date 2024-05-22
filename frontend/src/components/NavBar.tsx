// NavBar.tsx

import React from 'react';
import { NavLink as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import { Link as ScrollLink } from 'react-scroll';
import * as Scroll from 'react-scroll';
import './NavBar.css'; // Import your CSS file

const NavBar: React.FC = () => {
    const path = useLocation().pathname;
    const location = path.split("/")[1];
    const navigate = useNavigate();
    const scroller = Scroll.scroller;

    const goToPageAndScroll = async (selector: string) => {
        await navigate("/");
        await scroller.scrollTo(selector, {
        duration: 500,
        smooth: true,
        offset: -75,
        spy: true
        });
    };
    const handleClick = (event: React.MouseEvent<HTMLAnchorElement>, selector: string) => {
      event.preventDefault();
      goToPageAndScroll(selector);
    };
  return (
    <header id="navigation">
      <div className="navbar-wrapper">
      <nav>
        <ul className="nav-links"> {/* Add a class for styling */}
          {location !== "projects" && location !== "resume" ? (
            <>
                {" "}
                <ScrollLink to="home" spy={true} smooth={true} offset={-75} duration={500}>
                  Home
                </ScrollLink>
                <ScrollLink to="about" spy={true} smooth={true} offset={-75} duration={500}>
                  About
                </ScrollLink>
                <ScrollLink to="contact" spy={true} smooth={true} offset={-75} duration={500}>
                  Contact
                </ScrollLink>

                <RouterLink to="/projects">Projects</RouterLink>
                <RouterLink to="/resume">Resume</RouterLink>

            </>
          ) : (
            <>
                {" "}
                <a href="/" onClick={(event) => handleClick(event, 'home')}>Home</a>
                <a href="/" onClick={(event) => handleClick(event, 'about')}>About</a>
                <a href="/" onClick={(event) => handleClick(event, 'contact')}>Contact</a>                
                <RouterLink to="/projects">Projects</RouterLink>
                <RouterLink to="/resume">Resume</RouterLink>
            </>
          )}
        </ul>
      </nav>
      </div>
    </header>
  );
};

export default NavBar;
