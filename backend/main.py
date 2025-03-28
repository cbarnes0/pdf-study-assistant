import logging
import os, shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from .pdf_processor import extract_text_from_pdf

# Load environment variables and set up logging
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Ensure the uploads directory exists
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload-and-query/")
async def upload_and_query(file: UploadFile = File(...), query: str = Form(...)):
    try:
        # Save the uploaded PDF file
        file_path = UPLOAD_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract text and split into chunks if needed
        chunks = extract_text_from_pdf(str(file_path))
        full_text = "\n".join(chunks)
    except Exception as e:
        logger.error("Error during PDF processing", exc_info=True)
        return JSONResponse({"error": f"PDF processing failed: {e}"}, status_code=500)

    try:
        # Initialize the ChatGPT model via LangChain
        chat = ChatOpenAI(api_key=openai_api_key)
        message = HumanMessage(content=f"Document:\n{full_text}\n\nQuestion: {query}")
        response = chat([message])
    except Exception as e:
        logger.error("Error calling OpenAI API", exc_info=True)
        return JSONResponse({"error": f"OpenAI API call failed: {e}"}, status_code=500)

    return JSONResponse({"answer": response.content})
