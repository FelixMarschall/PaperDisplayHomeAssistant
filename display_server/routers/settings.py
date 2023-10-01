from fastapi import APIRouter, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["settings"],
)

templates = Jinja2Templates(directory="templates")

@dataclass
class SettingsData():
    size: str = Form(...)
    orientation: int = Form(...)

settings = SettingsData(
    size="5.65",
    orientation=0
)

@router.get("/settings")
async def read_settings(request: Request, response_model=SettingsData):
    accept_header = request.headers.get("Accept")

    if "text/html" in accept_header:
        return templates.TemplateResponse("settings.html", {"request": request})
    else:
        return settings
    
@router.post("/settings")
async def update_settings(request: Request, data: SettingsData = Depends()):
    logger.info(f"POST /settings size={data.size} orientation={data.orientation}")
    accept_header = request.headers.get("Accept")
    
    if "text/html" in accept_header:
        return templates.TemplateResponse("success.html", {"request": request})
    else:
        return {"message": "Success!"}