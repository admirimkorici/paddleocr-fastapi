from fastapi import FastAPI, File, UploadFile
from paddleocr import PaddleOCR
import uvicorn
import shutil
import os

app = FastAPI()

# Load the OCR model once during app startup
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # You can change lang to 'de', 'ch', etc.

@app.post("/ocr/")
async def read_image(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run OCR
    result = ocr.ocr(temp_file_path)

    # Delete temporary file
    os.remove(temp_file_path)

    # Extract text
    extracted_text = []
    for line in result:
        for box in line:
            extracted_text.append(box[1][0])

    return {"text": extracted_text}
