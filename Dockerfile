FROM python:3.12-slim

WORKDIR /app

# Install system dependencies required by PaddleOCR and PaddlePaddle
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install setuptools first
RUN pip install --upgrade pip setuptools wheel

COPY /app/requirements.txt ./app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
