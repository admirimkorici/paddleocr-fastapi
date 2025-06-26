# 🧠 PaddleOCR FastAPI App 🐳

A lightweight, production-ready OCR (Optical Character Recognition) microservice built using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) and [FastAPI](https://fastapi.tiangolo.com/), containerized with Docker for smooth deployment.

---

## 📸 Features

- 🔍 Extracts text from images using powerful PaddleOCR
- 🚀 FastAPI backend for blazing fast API response
- 🌐 RESTful API with built-in Swagger UI (`/docs`)
- 🐳 Fully Dockerized for easy setup and deployment
- 📤 Supports image upload and text detection from form-data
- 🧠 Multilingual OCR support with PaddleOCR models

---

## 📁 Project Structure

paddleocr-fastapi/
├── app/
│ ├── main.py # FastAPI entry point
| ├── requirements.txt # Python dependencies
├── Dockerfile # Docker image config
├── Docker-compose.yml # Docker Compose File
└── README.md # Project documentation


---

## 🚀 Getting Started

### 🧰 Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Git installed

---

### 🔧 Setup with Docker

```bash
# Clone the repository
git clone https://github.com/admirimkorici/paddleocr-fastapi.git
cd paddleocr-fastapi

# Execute Docker Compose Command
docker-compose up --build

Access the API documentation at:
👉 http://localhost:8000/docs

🔍 Example API Request
Send a POST request to the /ocr/ endpoint with an image:
curl -X POST http://localhost:8000/ocr/ \
  -F "file=@your-image.jpg"

Sample Response:
{
  "text": [
    "Invoice #12345",
    "Total: $89.00",
    "Thank you for your business"
  ]
}
