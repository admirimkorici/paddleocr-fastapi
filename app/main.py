from fastapi import FastAPI, File, UploadFile
from paddleocr import PaddleOCR
import shutil
import os
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend (Angular)
origins = [
    "http://localhost:4200",
    "https://yourfrontenddomain.com"  # Optional: add production domain too
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your upload directory and make sure it exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load the OCR model once during app startup
ocr = PaddleOCR(use_angle_cls=True, lang='sq')  # Change lang as needed

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    temp_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, temp_filename)

    # Save the uploaded file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run OCR on the saved file
    result = ocr.predict(file_path)

    # Delete the temporary file after OCR processing
    os.remove(file_path)

    # Extract recognized texts from OCR results
    texts = result[0]["rec_texts"] if result else []

    return {"text": texts}
