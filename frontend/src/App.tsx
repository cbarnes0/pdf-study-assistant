// src/App.tsx
import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [query, setQuery] = useState('');
  const [responseText, setResponseText] = useState('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

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
    <div id="root">
      <header className="header">
        <h1>PDF Study Assistant</h1>
      </header>
      <main>
        <div className="card">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="fileUpload">Upload PDF:</label>
              <input
                id="fileUpload"
                type="file"
                accept="application/pdf"
                onChange={handleFileChange}
                className="input-field"
              />
            </div>
            <div className="form-group">
              <label htmlFor="queryInput">Query:</label>
              <input
                id="queryInput"
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter your query..."
                className="input-field"
              />
            </div>
            <button type="submit" className="submit-button">Submit</button>
          </form>
          {responseText && (
            <div className="response-section">
              <h2>Response:</h2>
              <p>{responseText}</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default App;
