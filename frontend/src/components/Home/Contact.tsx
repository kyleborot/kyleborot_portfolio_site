// Contact.tsx

import React from 'react';

interface Props {
    id: string;
}

const Contact: React.FC<Props> = ({ id }) => {
  return (
    <div id={id}>
      <h2>Contact</h2>
      {/* Add your Contact content here */}
    </div>
  );
}

export default Contact;
