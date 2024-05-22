// About.tsx

import React from 'react';
import { Element } from 'react-scroll';
import './HomeComponent.css'

const About: React.FC = () => {
    const centerStyle: React.CSSProperties = {
        textAlign: 'center'
      };
    const flexColumnStyle: React.CSSProperties = {
        flexDirection: 'column'
    };
  return (
    <Element name="about">
        <div className="container">
            <div style={flexColumnStyle}>
            <div style={centerStyle}>
                <h1>About Me</h1>
                <p><strong>engineer</strong>, /ˌɛnʤəˈniɚ/, <em>noun</em></p>
                <p>a person who has scientific training and who designs and builds complicated products, machines, systems, or structures</p>
            </div>
            <div className="text-section">
                <p>
                As a student of mechanical engineering and computer science, 
                I have had the opportunity to engage in a variety of engineering disciplines and industries. 
                From civil to solar, defense and nautical, I have been able to sharpen my engineering principles
                and enhance my software engineering capabilities to be a multi-faceted team player
                </p>
            </div>
            </div>
            <div className="image-container">
            <img src="/home_photo.png" alt="profile photo"/>
            </div>
        </div>
    </Element>
  );
}

export default About;
