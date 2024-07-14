// Projects.tsx

import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'
import axios from 'axios';
import './Projects.css'

interface Project {
  id: number;
  name: string;
  shortDescription: string;
  longDescription: string;
  isDemo: boolean;
  projectURL: string;
  photoURL: string;
  createdDate: string;
  createdLocation: string;
  techUsed: string;
}

const Projects: React.FC = () => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect (() => {
    axios.get('http://127.0.0.1:5000/api/projects')
    .then(response => {
      setProjects(response.data);
      setLoading(false);
    })
    .catch(error => {
      setError(error.message);
      setLoading(false);
    })
  }, []);

  if (loading) {
    return <div>Loading...</div>
  }
  if (error) {
    return <div>Error: {error}</div>
  }

  return (
    <div>
      <h1>Projects</h1>
       <div className="project-cards">
        {projects.map(project => (
          <div key={project.id} className="project-card">
            <h2>{project.name}</h2>
            <p>{project.shortDescription}</p>
            <p><strong>Technologies Used:</strong> {project.techUsed}</p>
            {project.projectURL.startsWith('http') ? (
              <a href={project.projectURL} target="_blank" rel="noopener noreferrer">
                <button className="project-button">View Project</button>
              </a>
            ) : (
              <Link to={project.projectURL}>
                <button className="project-button">View Project</button>
              </Link>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Projects;
