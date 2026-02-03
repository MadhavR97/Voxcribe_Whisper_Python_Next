# Voxscribe Backend Setup Guide

This guide explains how to set up and run the Voxscribe backend after cloning the repository.

## Prerequisites

- Python 3.8+
- pip package manager
- ffmpeg installed and available in PATH

## Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/MadhavR97/Voxcribe_Python_Whisper_Backend.git
   ```

2. **Navigate to the backend directory**
   ```bash
   cd Voxscribe_Python_Whisper_Backend/backend
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install ffmpeg (required for audio processing)**
   - On Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
   - On macOS with Homebrew: `brew install ffmpeg`
   - On Windows with Chocolatey: `choco install ffmpeg`

5. **Run the backend service**
   ```bash
   uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Verify the service is running**
   The backend will be available at `http://localhost:8000`
   You can test the transcription endpoint at `http://localhost:8000/transcribe`

## Endpoints

- `POST /transcribe` - Transcribe audio files using Whisper

## Notes

- Make sure ffmpeg is installed as it's required for audio processing
- The service runs on port 8000 by default
- The backend needs to be running before starting the frontend
- For production deployments, consider security aspects like restricting CORS origins