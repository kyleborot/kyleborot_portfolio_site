// ProjectDetail.tsx

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './ProjectDetail.css';

interface Project {
  id: number;
  name: string;
  longDescription: string;
  projectURL: string;
  photoURL: string;
  createdDate: string;
  createdLocation: string;
  techUsed: string;
}

const ProjectDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [project, setProject] = useState<Project | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/projects/${id}`)
      .then(response => {
        setProject(response.data);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="project-detail">
      <h1>{project?.name}</h1>
      <img src={project?.photoURL} alt={project?.name} className="project-photo" />
      <p>{project?.longDescription}</p>
      <p><strong>Technologies Used:</strong> {project?.techUsed}</p>
    </div>
  );
};

export default ProjectDetail;
