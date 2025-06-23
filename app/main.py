from fastapi import FastAPI, UploadFile, File
from paddleocr import PaddleOCR
from PIL import Image
import io
import numpy as np

app = FastAPI()

# Initialize PaddleOCR with multilingual support
ocr = PaddleOCR(use_angle_cls=True, lang='multilang')

@app.get("/")
async def root():
    return {"message": "PaddleOCR FastAPI running"}

@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    # Read file bytes
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes))

    # PaddleOCR works with image path or numpy array, convert to numpy array
    img_np = np.array(img)

    # Run OCR
    result = ocr.ocr(img_np, cls=True)

    # Format results
    texts = []
    for line in result[0]:
        text = line[1][0]
        confidence = line[1][1]
        texts.append({"text": text, "confidence": confidence})

    return {"results": texts}
