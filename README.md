# PDF Study Assistant

PDF Study Assistant is a web application that allows users to upload PDF documents, extract their content, and query the information using an AI-powered backend. Eventually, the app will also support additional features like generating flashcards from the PDF content.

## Features

- **FastAPI Backend:** Processes PDF uploads, extracts text, and integrates with OpenAI for answering queries.
- **React Frontend (Vite + TypeScript):** Provides a user-friendly interface for uploading PDFs and viewing responses.
- **Unit Tested:** Core functionality, such as PDF extraction, is covered by tests.

## Prerequisites

- **Python 3.8+** (for the FastAPI backend)
- **Node.js & npm** (for the React frontend)

## Setup

### Backend

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/cbarnes0/pdf-study-assistant.git
   cd pdf-study-assistant
   ```

2. **Create and Activate a Virtual Environment:**

   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install Python Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Run the FastAPI Backend:**

   ```bash
   uvicorn backend.main:app --reload
   ```
   The backend will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Frontend

1. **Navigate to the Frontend Folder:**

   ```bash
   cd frontend
   ```

2. **Install Node Dependencies:**

   ```bash
   npm install
   ```

3. **Start the Development Server:**

   ```bash
   npm run dev
   ```
   The frontend will typically run on [http://localhost:3000](http://localhost:3000). (Note: The Vite configuration is set up to proxy API requests to the FastAPI backend.)

## Testing

To run the backend unit tests, navigate to the project root and run:

```bash
python -m unittest discover tests
```

## Usage

- **Using the Frontend:**  
  Open your browser and go to [http://localhost:3000](http://localhost:3000). Use the provided form to upload a PDF and enter a query. The application will send your data to the backend and display the AI-generated response.

- **API Documentation:**  
  You can also view the interactive API docs provided by FastAPI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Future Enhancements

- **Flashcards Generation:** Create flashcards based on the PDF content.
- **Enhanced UI/UX:** Further polish the frontend design.
- **User Features:** Add features like user authentication, query history, etc.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.

