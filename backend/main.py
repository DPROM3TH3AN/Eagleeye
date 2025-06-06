from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.routers import chat, tracking, numbers
import os
import logging
from fastapi.responses import HTMLResponse

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logging.debug(f"Base Directory: {BASE_DIR}")

app = FastAPI(
    title="Eagle Eye Tracking System",
    description="API for chat, device tracking (including IMEI), phone analysis, realtime updates, and NextBillion AI integration.",
    version="1.0.0"
)

# Include routers for different services
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(tracking.router, prefix="/tracking", tags=["Tracking"])
app.include_router(numbers.router, prefix="/numbers", tags=["Numbers"])

# Mount static files and templates with absolute paths
static_dir = os.path.join(BASE_DIR, "frontend/static")
templates_dir = os.path.join(BASE_DIR, "frontend/templates")
logging.debug(f"Static Directory: {static_dir}")
logging.debug(f"Templates Directory: {templates_dir}")

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "title": "Eagle Eye Dashboard"
        }
    )

# Add routes for each main section
@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "title": "Chat System"
        }
    )

@app.get("/tracking", response_class=HTMLResponse)
async def tracking_page(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "title": "Tracking System"
        }
    )

@app.get("/numbers", response_class=HTMLResponse)
async def numbers_page(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {
            "request": request,
            "title": "Number Analysis"
        }
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)