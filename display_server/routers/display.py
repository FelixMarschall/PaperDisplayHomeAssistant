from fastapi import APIRouter, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from dataclasses import dataclass
import logging
import base64

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["display"],
)

templates = Jinja2Templates(directory="templates")

@router.get("/display")
async def read_display(request: Request):
    accept_header = request.headers.get("Accept")

    if "text/html" in accept_header:
        return templates.TemplateResponse("display.html", {"request": request, "image": ()})
    else:
        return {"message": "image with the "}

@router.post("/display/image")
async def get_display_image():
    # TODO: get image from display controller
    pass