from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from paddleocr import PaddleOCR
import shutil
import os
import uuid

app = FastAPI()

# Load the OCR model once during app startup
ocr = PaddleOCR(use_angle_cls=True, lang='sq')  # You can change lang to 'de', 'ch', etc.

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    temp_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, temp_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run OCR
    result = ocr.predict(temp_file_path)

    # Delete temporary file
    os.remove(temp_file_path)

    return {"text": result[0]["rec_texts"]}
