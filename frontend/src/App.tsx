// App.tsx

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NavBar from './components/NavBar';
import HomeContainer from './components/Home/HomeContainer';
import Projects from './components/Projects/Projects';
import Resume from './components/Resume/Resume.tsx';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <NavBar />
        <Routes>
          <Route path="/" element={<HomeContainer />} />
          <Route path="/projects" Component={Projects} />
          <Route path="/resume" Component={Resume} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
