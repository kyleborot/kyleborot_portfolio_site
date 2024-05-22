// Home.tsx

import React from 'react';
import { NavLink as RouterLink, useLocation, useNavigate } from 'react-router-dom';
import * as Scroll from 'react-scroll';
import './HomeComponent.css'

const Home: React.FC = () => {
  
  const navigate = useNavigate();

  const goToPage = (page : string) => {
    navigate(page);
  };

  return (
    <div className="container">
      <div className="text-buttons">
        <h1>Hello!</h1> 
        <h1>I'm Kyle, </h1>
        <h1>an engineer.</h1>
        <h1>I made this website.</h1>
        <h2>like, seriously.</h2>
        <div className="buttons">
          <button onClick={() => goToPage("projects")}>Explore</button>
          <button onClick={() => goToPage("contact")}>Let's work together!</button>
        </div>
      </div>
        <div className="image-container">
          <img src="/home_photo.png" alt="profile photo"/>
        </div>
    </div>
  );
}

export default Home;
