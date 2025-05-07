from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from app import create_svg
import os
from pathlib import Path

# Ensure static directory exists
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

app = FastAPI(title="SVG Animation Viewer")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        # Generate new SVG
        svg_file = create_svg()
        if not os.path.exists(svg_file):
            raise HTTPException(status_code=500, detail="Failed to create SVG file")
        
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "title": "SVG Animation Viewer"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/regenerate")
async def regenerate():
    try:
        svg_file = create_svg()
        if not os.path.exists(svg_file):
            raise HTTPException(status_code=500, detail="Failed to create SVG file")
        return {"status": "success", "message": "SVG regenerated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 