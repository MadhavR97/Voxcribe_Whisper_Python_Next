from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from whisper_service import transcribe_audio

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    return transcribe_audio(audio_bytes)