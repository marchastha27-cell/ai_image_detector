from fastapi import FastAPI

app = FastAPI(title="AI vs Real Image Detector")

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}
