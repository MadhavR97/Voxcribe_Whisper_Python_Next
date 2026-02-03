import subprocess
import tempfile
import shutil
import os
import whisper
import threading

# -----------------------------
# FFmpeg check (Render-safe)
# -----------------------------
FFMPEG_EXE = shutil.which("ffmpeg")
if not FFMPEG_EXE:
    raise RuntimeError("ffmpeg not found. Make sure ffmpeg is available on the system.")

# -----------------------------
# Whisper lazy-load (CRITICAL)
# -----------------------------
_model = None
_model_lock = threading.Lock()


def get_model():
    """
    Load Whisper model only once.
    This prevents OOM and startup crashes on Render.
    """
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                # Use tiny model for Render free tier
                _model = whisper.load_model("tiny")
    return _model


# -----------------------------
# Audio conversion
# -----------------------------
def convert_to_wav(input_path: str) -> str:
    """
    Convert any audio format to 16kHz mono WAV
    """
    wav_path = input_path + ".wav"

    subprocess.run(
        [
            FFMPEG_EXE,
            "-y",
            "-i", input_path,
            "-ac", "1",
            "-ar", "16000",
            "-acodec", "pcm_s16le",
            wav_path,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return wav_path


# -----------------------------
# Transcription function
# -----------------------------
def transcribe_audio(file_bytes: bytes):
    """
    Transcribe uploaded audio bytes using Whisper
    """
    model = get_model()

    input_audio_path = None
    wav_path = None

    try:
        # Save uploaded bytes to temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file_bytes)
            input_audio_path = tmp.name

        # Convert to WAV
        wav_path = convert_to_wav(input_audio_path)

        # Transcribe
        result = model.transcribe(
            wav_path,
            word_timestamps=True,
            fp16=False,  # IMPORTANT: CPU-only safety
        )

        words = []
        for seg in result.get("segments", []):
            for w in seg.get("words", []):
                words.append({
                    "word": w["word"],
                    "start": float(w["start"]),
                    "end": float(w["end"]),
                })

        full_text = " ".join(w["word"] for w in words)

        return {
            "text": full_text,
            "words": words,
        }

    finally:
        # Cleanup temp files
        if input_audio_path and os.path.exists(input_audio_path):
            os.remove(input_audio_path)

        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)
