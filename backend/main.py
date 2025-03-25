from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import shutil
from pathlib import Path
from pypdf import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Directory for uploaded files
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload-and-query/")
async def upload_and_query(file: UploadFile = File(...), query: str = Form(...)):
    # Save the uploaded PDF file locally
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extract text from the PDF using pypdf
    text = ""
    with file_path.open("rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:  # Check in case extraction returns None
                text += page_text + "\n"

    # Initialize the ChatGPT model via LangChain
    chat = ChatOpenAI(api_key=openai_api_key)
    
    # Construct a message combining the PDF content and user query
    message = HumanMessage(content=f"Document:\n{text}\n\nQuestion: {query}")
    response = chat([message])
    
    # Return the answer from the model
    return JSONResponse({"answer": response.content})
