// src/App.tsx
import React, { useState } from 'react';

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [query, setQuery] = useState('');
  const [responseText, setResponseText] = useState('');

  // Capture file selection
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  // Handle form submission
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!file || !query) {
      alert('Please provide a PDF file and a query.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('query', query);

    try {
      // API request; the proxy in vite.config.ts forwards this to your backend
      const res = await fetch('/upload-and-query/', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      setResponseText(data.answer || data.error || 'No response received.');
    } catch (error) {
      console.error('Error:', error);
      setResponseText('An error occurred while processing your request.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>PDF Study Assistant</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Upload PDF:</label>
          <input type="file" accept="application/pdf" onChange={handleFileChange} />
        </div>
        <div style={{ marginTop: '10px' }}>
          <label>Query:</label>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your query..."
          />
        </div>
        <button type="submit" style={{ marginTop: '10px' }}>Submit</button>
      </form>
      {responseText && (
        <div style={{ marginTop: '20px' }}>
          <h2>Response:</h2>
          <p>{responseText}</p>
        </div>
      )}
    </div>
  );
};

export default App;
