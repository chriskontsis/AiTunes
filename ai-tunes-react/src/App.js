import React, { useState } from 'react';
import './App.css';
import headphones from './headphones.png';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [showTrack, setShowTrack] = useState(false);
  const [selectedTrack, setSelectedTrack] = useState('');

  const tracks = [
    "https://open.spotify.com/track/0CTwVocVcXONwAbRxk4r24?si=7f1e35b574704251",
    "https://open.spotify.com/track/3pEuO9J2MTEmec8kUfYYvl?si=8287fe8a19ed492f",
    "https://open.spotify.com/track/65gFUBEh59KEBCznPKQnbG?si=7eb75dded8994596",
    "https://open.spotify.com/track/5bFuHlXKw66Uu2cHKn5bf8?si=5a23fba2295a401a",
    "https://open.spotify.com/track/7dQeS4ErW1iWvnKdrtKwKr?si=b1c3d7df1b6d489e",
    "https://open.spotify.com/track/11LmqTE2naFULdEP94AUBa?si=06d30cd919774c48",
    "https://open.spotify.com/track/1G391cbiT3v3Cywg8T7DM1?si=fb28b31071db44fc",
    "https://open.spotify.com/track/5Z3trOR982mBrJcPfrLUsq?si=52963b4c04164a7e"
  ];

  const handleSubmit = () => {
    console.log(inputValue);

    const randomTrack = tracks[Math.floor(Math.random() * tracks.length)];
    setSelectedTrack(randomTrack);

    setShowTrack(true);

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
          title="Spotify Embedded Track"
          style={{borderRadius: '12px', marginTop: '20px'}} 
          src={selectedTrack.replace("open.spotify.com/track", "open.spotify.com/embed/track")} 
          width="700px" 
          height="352" 
          frameBorder="0" 
          allowFullScreen 
          allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
          loading="lazy">
        </iframe>
      )}
    </div>
  );
}


// #comments
export default App;
