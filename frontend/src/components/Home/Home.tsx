// Home.tsx

import React from 'react';
import { Link } from 'react-scroll';

const Home: React.FC = () => {
  return (
    <div>
      <h1>Home</h1>
      <Link to="about" smooth={true} duration={500}>About</Link>
      <Link to="contact" smooth={true} duration={500}>Contact</Link>
    </div>
  );
}

export default Home;
