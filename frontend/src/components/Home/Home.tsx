// Home.tsx

import React from 'react';
import { NavLink as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import { Link as ScrollLink } from 'react-scroll';
import * as Scroll from 'react-scroll';

const Home: React.FC = () => {
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
    <div>
      <h1>Hello!</h1> 
      <h1>I'm Kyle, </h1>
      <h1>an Engineer</h1>
      <img src="/home_photo.png" alt="profile photo"/>
      <button>Learn what that means</button>
      <button>Let's work together!</button>

    </div>
  );
}

export default Home;
