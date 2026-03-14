from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/api")
def home():
    return {"status": "Backend is Running", "message": "ElevenLabs Ready"}

@app.get("/api/voice-test")
def test():
    key = os.getenv("ELEVENLABS_API_KEY")
    return {"key_detected": bool(key)}

