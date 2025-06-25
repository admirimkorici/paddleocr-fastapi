from fastapi import FastAPI, File, UploadFile
from paddleocr import PaddleOCR
import uvicorn
import shutil
import os

app = FastAPI()

# Load the OCR model once during app startup
ocr = PaddleOCR(use_angle_cls=True, lang='sq')  # You can change lang to 'de', 'ch', etc.

@app.post("/ocr/")
async def read_image(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run OCR
    result = ocr.predict(temp_file_path)

    # Delete temporary file
    os.remove(temp_file_path)

    return {"text": result[0]["rec_texts"]}
