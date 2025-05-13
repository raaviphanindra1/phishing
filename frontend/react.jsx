// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);

  const checkURL = async () => {
    const res = await axios.post('/api/check-url', { url });
    setResult(res.data);
  };

  return (
    <div className="App">
      <h2>Phishing Website Detector</h2>
      <input value={url} onChange={e => setUrl(e.target.value)} placeholder="Enter a URL" />
      <button onClick={checkURL}>Check</button>
      {result && (
        <div>
          <h3>Result:</h3>
          <p>{result.suspicious ? 'Suspicious' : 'Safe'}</p>
          <ul>{result.reason.map((r, i) => <li key={i}>{r}</li>)}</ul>
        </div>
      )}
    </div>
  );
}

export default App;
