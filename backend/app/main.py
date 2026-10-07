from fastapi import FastAPI

app = FastAPI(
    title="AI Prompt Injection Firewall",
    description="A security layer for detecting prompt injection attacks in LLM applications.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Prompt Injection Firewall API",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "AI Prompt Injection Firewall",
        "phase": "Phase 1"
    }