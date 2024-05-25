// About.tsx

import React from 'react';
import { Element } from 'react-scroll';
import './HomeComponent.css'
import { useNavigate } from 'react-router-dom';

const About: React.FC = () => {
    const centerStyle: React.CSSProperties = {
        textAlign: 'center'
      };
    const flexColumnStyle: React.CSSProperties = {
        flexDirection: 'column'
    };
    const bottomPadding: React.CSSProperties = {
        paddingBottom: '100px'
      };

    const navigate = useNavigate();

    const goToPage = (page : string) => {
      navigate(page);
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
                            engineering progression. Click below to explore what I have to offer in my engineering pursuits.
                        </p>
                    </div>
                </div>
                <div className="text-buttons" style={Object.assign(centerStyle, bottomPadding)}>
                        <button onClick={() => goToPage("projects")}>Explore</button>
                </div>
            </div>
        </Element>
        );
}

export default About;
