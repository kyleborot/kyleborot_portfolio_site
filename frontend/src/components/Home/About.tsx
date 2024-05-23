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
            <div className="about-container">
                <div className="about-header">
                    <h1>About</h1>
                    <p><strong>engineer</strong>, /ˌɛnʤəˈniɚ/, <em>noun</em></p>
                </div>
                <div className="about-content">
                    <div className="about-img-container">
                        <img src="/about_gif.gif" alt="man using software"/>
                    </div>
                    <div className="text-section">
                        <p>
                            As a student of mechanical engineering and computer science, 
                            I have had the opportunity to engage in a variety of engineering disciplines and industries. 
                            From <strong>civil</strong> to <strong>solar</strong>, <strong>defense</strong> and <strong>nautical</strong>, I have been able to sharpen my engineering principles
                            and enhance my software engineering capabilities to be a multi-faceted team player.
                        </p>
                        <p>
                            This website not only showcases my 
                            experience but also stands as a project in its own right. 
                            As a full-stack application, it demonstrates my technical skills through interactive features,
                            including a secure user login system, a GPT-powered chatbot, and a visualized timeline of my 
                            engineering progression. Each element has been meticulously crafted to highlight my proficiency
                            in modern web development technologies, providing an engaging and informative experience for visitors.
                        </p>
                    </div>
                </div>
            </div>
        </Element>
        );
}

export default About;
