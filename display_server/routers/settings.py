from fastapi import APIRouter, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
import logging

from controller.settings_controller import Settings, SettingsData


logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["settings"],
)

templates = Jinja2Templates(directory="templates")


@router.get("/settings")
async def read_settings(request: Request, response_model=SettingsData):
    """Read the current settings from the display controller."""
    accept_header = request.headers.get("Accept")

    if "text/html" in accept_header:
        return templates.TemplateResponse("settings.html", {"request": request})
    return Settings().setting_data


@router.post("/settings")
async def update_settings(request: Request, data: SettingsData = Depends()):
    """Update the settings on the display controller."""
    logger.info("POST /settings size=%s", data)
    accept_header = request.headers.get("Accept")

    if "text/html" in accept_header:
        return templates.TemplateResponse("success.html", {"request": request})
    else:
        return {"message": "Success!"}
