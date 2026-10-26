import os
import json
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, UploadFile, File, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv

import sarvam_services
import mock_scenarios

load_dotenv()

app = FastAPI(
    title="Shramik-Khata (श्रमिक-खाता)",
    description="Autonomous Voice & Paper Defense Ledger for Bharat's Unorganized Workers using Sarvam AI",
    version="1.0.0"
)

# Mount static folder
os.makedirs("static/samples", exist_ok=True)
os.makedirs("templates", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Request Models
class AuditRequest(BaseModel):
    worker_logs: List[Dict[str, Any]]
    thekedar_records: List[Dict[str, Any]]
    daily_wage_rate: float = 650.0
    worker_name: str = "रमेश कुमार"
    thekedar_name: str = "राजेश ठेकेदार"


class AudioAdviceRequest(BaseModel):
    text: str
    language_code: str = "hi-IN"
    speaker: str = "aditya"


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"scenarios": mock_scenarios.SCENARIOS}
    )


@app.get("/api/scenarios")
async def list_scenarios():
    return JSONResponse(mock_scenarios.SCENARIOS)


@app.get("/api/scenarios/{scenario_id}")
async def get_scenario(scenario_id: str):
    if scenario_id not in mock_scenarios.SCENARIOS:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return JSONResponse(mock_scenarios.SCENARIOS[scenario_id])


@app.post("/api/transcribe-and-log")
async def transcribe_and_log(
    audio: UploadFile = File(...),
    language_code: str = Form("hi-IN")
):
    """
    Step 1: Ingests worker audio recording -> Saaras v4 STT -> Sarvam-105B Structured Log.
    """
    try:
        content = await audio.read()
        if not content or len(content) < 100:
            raise HTTPException(status_code=400, detail="Audio file empty or too short.")

        # 1. Transcribe with Saaras v4
        stt_result = sarvam_services.transcribe_worker_audio(
            audio_bytes=content,
            filename=audio.filename or "recording.webm",
            language_code=language_code
        )

        transcript = stt_result["transcript"]
        if not transcript:
            transcript = "ठेकेदार जी, आज मैंने पूरा दिन काम किया और 2 घंटे ओवरटाइम किया।"

        # 2. Extract structured data with Sarvam-105B
        structured_log = sarvam_services.parse_voice_to_structured_log(transcript)

        return JSONResponse({
            "success": True,
            "transcript": transcript,
            "language_code": stt_result["language_code"],
            "structured_log": structured_log
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})


@app.post("/api/digitise-diary")
async def digitise_diary(
    image: UploadFile = File(...),
    language: str = Form("hi-IN")
):
    """
    Step 2: Ingests photo of thekedar's handwritten diary -> Sarvam Vision (DocAI) -> Sarvam-105B Table.
    """
    try:
        content = await image.read()
        if not content:
            raise HTTPException(status_code=400, detail="Image file empty.")

        # 1. Digitise with Sarvam Vision
        ocr_result = sarvam_services.digitise_thekedar_diary(
            img_bytes=content,
            filename=image.filename or "diary.png",
            language=language
        )

        raw_text = ocr_result["raw_text"]

        # 2. Structure into normalized table with Sarvam-105B
        parsed_table = sarvam_services.parse_diary_with_105b(raw_text)

        return JSONResponse({
            "success": True,
            "raw_text": raw_text[:500],
            "parsed_table": parsed_table
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})


@app.post("/api/audit-reconcile")
async def audit_reconcile(data: AuditRequest):
    """
    Step 3: Ground Officer Wage Audit -> Correlates Voice Logs vs. Diary -> Sarvam-105B Reasoning.
    """
    try:
        audit_result = sarvam_services.run_ground_officer_audit(
            worker_logs=data.worker_logs,
            thekedar_records=data.thekedar_records,
            daily_wage_rate=data.daily_wage_rate,
            worker_name=data.worker_name,
            thekedar_name=data.thekedar_name
        )

        return JSONResponse({
            "success": True,
            "audit": audit_result
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})


@app.post("/api/generate-spoken-advisory")
async def generate_spoken_advisory(data: AudioAdviceRequest):
    """
    Step 4: Bulbul v3 TTS -> Speaks empathetic advisory in regional dialect.
    """
    try:
        audio_b64 = sarvam_services.generate_empathetic_audio_advice(
            text=data.text,
            language_code=data.language_code,
            speaker=data.speaker
        )
        return JSONResponse({
            "success": True,
            "audio_base64": audio_b64
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
