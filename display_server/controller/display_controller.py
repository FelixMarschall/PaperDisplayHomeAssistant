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

import logging

# from waveshare_epd import epd5in65f
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logger = logging.getLogger(__name__)


class DisplayController:
    current_display: str = None

    def __init__(self):
        pass
