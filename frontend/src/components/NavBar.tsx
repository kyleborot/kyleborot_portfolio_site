// NavBar.tsx

import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const NavBar: React.FC = () => {
  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand href="/">React TS Website</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <LinkContainer to="/">
            <Nav.Link>Home</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/projects">
            <Nav.Link>Projects</Nav.Link>
          </LinkContainer>
          <LinkContainer to="/resume">
            <Nav.Link>Resume</Nav.Link>
          </LinkContainer>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavBar;
