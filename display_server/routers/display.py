from fastapi import APIRouter, Form, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from dataclasses import dataclass
import logging
import base64

import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic"
)
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd5in65f
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

router = APIRouter(
    tags=["display"],
)

templates = Jinja2Templates(directory="templates")


@router.get("/display")
async def read_display(request: Request):
    accept_header = request.headers.get("Accept")

    if "text/html" in accept_header:
        return templates.TemplateResponse(
            "display.html", {"request": request, "image": ()}
        )
    else:
        return {"message": "image with the "}


@router.get("/display/init")
async def init():
    """Starts init process of the paper display."""
    try:
        epd = epd5in65f.EPD()
        logging.info("Init display...")
        epd.init()
        return "init done."
    except IOError as e:
        logging.error(e)


@router.get("/display/clear")
async def init():
    """Clears display from images and text."""
    try:
        epd = epd5in65f.EPD()
        epd.init()
        logging.info("Clear display...")
        epd.Clear()
        return "display clear."
    except IOError as e:
        logging.error(e)


@router.get("/display/test")
async def test():
    """Test display with text and images."""
    try:
        logging.info("epd5in65f Demo")

        epd = epd5in65f.EPD()
        epd.init()
        font24 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 24)
        font18 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 18)
        font30 = ImageFont.truetype(os.path.join(picdir, "Font.ttc"), 40)

        logging.info("1.Drawing on the Horizontal image...")
        Himage = Image.new(
            "RGB", (epd.width, epd.height), 0xFFFFFF
        )  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        draw.text((10, 0), "Hello AIFB!", font=font30, fill=0)
        draw.text(
            (10, 200),
            "Scheint zu funktionieren!",
            font=font24,
            fill=0,
        )
        epd.display(epd.getbuffer(Himage))

        logging.info("3.read bmp file")
        Himage = Image.open(os.path.join(picdir, "5in65f2.bmp"))
        epd.display(epd.getbuffer(Himage))

        return "success"
    except IOError as e:
        logging.error(e)


# @router.post("/display/website")
# async def curl_website_image(data: Form(...)):
#     """Curls a website and returns the image."""
#     website = data["website"]
#     logging.info(f"curling website {website}")


@router.post("/display/image")
async def get_display_image():
    # TODO: get image from display controller
    pass
