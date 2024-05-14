// HomeContainer.tsx

import React from 'react';
import Home from './Home';
import About from './About';
import Contact from './Contact';

const HomeContainer: React.FC = () => {
  return (
    <div>
      <Home />
      <About />
      <Contact id="contact"/>
    </div>
  );
}

export default HomeContainer;
