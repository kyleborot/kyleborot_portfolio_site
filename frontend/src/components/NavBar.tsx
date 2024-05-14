// NavBar.tsx

import React from 'react';
import { NavLink as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import { Link as ScrollLink } from 'react-scroll';
import * as Scroll from 'react-scroll';

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
  return (
<header id="navigation">
      <nav>
        <ul>
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
                <button onClick={() => goToPageAndScroll("home")}>Home</button>
                <button onClick={() => goToPageAndScroll("about")}>About</button>
                <button onClick={() => goToPageAndScroll("contact")}>Contact</button>
                <RouterLink to="/projects">Projects</RouterLink>
                <RouterLink to="/resume">Resume</RouterLink>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default NavBar;
