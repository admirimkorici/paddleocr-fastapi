from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from paddleocr import PaddleOCR
import shutil
import os
import uuid

app = FastAPI()

ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Change `lang` to 'de', 'fr', etc.

UPLOAD_DIR = "/tmp/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    temp_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, temp_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = ocr.ocr(file_path)
    os.remove(file_path)

    texts = []
    for line in result[0]:
        text = line[1][0]
        texts.append(text)

    return JSONResponse({"extracted_text": texts})
