import React, { useState } from 'react';
import './App.css';
import headphones from './headphones.png';

function App() {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = () => {
    // You can add any logic here to handle the input value if needed
    console.log(inputValue);
    
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
    </div>
  );
}

export default App;
