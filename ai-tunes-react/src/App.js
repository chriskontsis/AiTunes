import React, { useState } from 'react';
import './App.css';
import headphones from './headphones.png';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [showTrack, setShowTrack] = useState(false);

  const handleSubmit = () => {
    console.log(inputValue);
    
    // Show the embedded track
    setShowTrack(true);
    
    // Clearing the input box after submission
    setInputValue('');
  };

  return (
    <div className="container">
      <img src={headphones} alt="Headphones Icon" className="headphones-icon" />
      <div className="title">AiTunes</div>
      <input 
        type="text" 
        className="input-box"
        value={inputValue} 
        onChange={(e) => setInputValue(e.target.value)} 
        placeholder="Give us an idea"
      />
      <button onClick={handleSubmit} className="submit-button">Submit</button>
      {showTrack && (
        <iframe 
          style={{borderRadius: '12px', marginTop: '20px'}} 
          src="https://open.spotify.com/embed/track/4Uiw0Sl9yskBaC6P4DcdVD?utm_source=generator" 
          width="700px" 
          height="352" 
          frameBorder="1" 
          allowfullscreen="1" 
          allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
          loading="lazy">
        </iframe>
      )}
    </div>
  );
}

export default App;
