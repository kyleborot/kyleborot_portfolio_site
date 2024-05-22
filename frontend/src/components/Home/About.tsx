// About.tsx

import React from 'react';
import { Element } from 'react-scroll';
import './HomeComponent.css'

const About: React.FC = () => {
  return (
    <Element name="about">
        <div className="container">
            <div className="text-section">
                <p>
                    Hi, I'm Kyle Borot, a Mechanical Engineering and Computer Science student at Florida International University. 
                    Over my college years, I've worked in various engineering fields, including civil, mechanical, and software engineering. 
                    I've gained hands-on experience in industries like infrastructure, solar energy, defense, and nautical engineering. 
                    This mix of experiences has given me a solid grasp of engineering principles and made me a flexible engineer ready to tackle any challenge.
                </p>
                <p>
                    When I'm not immersed in my studies or projects, you'll find me cheering on the Miami Dolphins or trying out new foods. 
                    I'm a huge American football fan and love exploring different cuisines. 
                    Lately, I've also been diving into the world of financial markets, learning about trading and investment strategies. 
                    These interests help me balance my busy schedule and keep me curious and motivated.
                </p>
            </div>
            <div className="image-container">
                {/* Future image can be included here */}
                {/* <img src="/about_photo.png" alt="Kyle Borot"/> */}
            </div>
        </div>
    </Element>
  );
}

export default About;
