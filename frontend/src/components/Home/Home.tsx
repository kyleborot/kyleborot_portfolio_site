// Home.tsx

import React from 'react';
import { NavLink as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import * as Scroll from 'react-scroll';
import './HomeComponent.css'

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
    <div className="container">
      <div className="text-buttons">
        <h1>Hello!</h1> 
        <h1>I'm Kyle, </h1>
        <h1>an engineer.</h1>
        <div className="buttons">
          <button onClick={() => goToPageAndScroll("about")}>Learn what that means</button>
          <button onClick={() => goToPageAndScroll("contact")}>Let's work together!</button>
        </div>
      </div>
        <div className="image-container">
          <img src="/home_photo.png" alt="profile photo"/>
        </div>
    </div>
  );
}

export default Home;
