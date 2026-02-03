import subprocess
import tempfile
import shutil
import os
import whisper

FFMPEG_EXE = shutil.which("ffmpeg")
if not FFMPEG_EXE:
    raise RuntimeError("ffmpeg not found")

model = whisper.load_model("base")


def convert_to_wav(input_path: str) -> str:
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


def transcribe_audio(file_bytes: bytes):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file_bytes)
        input_audio_path = tmp.name

    wav_path = None
    try:
        wav_path = convert_to_wav(input_audio_path)

        result = model.transcribe(
            wav_path,
            word_timestamps=True,
        )

        words = []
        for seg in result.get("segments", []):
            for w in seg.get("words", []):
                words.append({
                    "word": w["word"],
                    "start": w["start"],
                    "end": w["end"],
                })

        full_text = " ".join(w["word"] for w in words)

        return {
            "text": full_text,
            "words": words,
        }

    finally:
        if os.path.exists(input_audio_path):
            os.remove(input_audio_path)
        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)
