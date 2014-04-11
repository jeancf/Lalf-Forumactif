import png
import subprocess

from lalf.exceptions import *
from lalf.config import config

def toolong(img):
    """
    Returns true if the email displayed in the image img is too long to
    be displayed entirely
    """
    reader = png.Reader(filename=img)
    w, h, pixels, metadata = reader.read_flat()

    for i in range(w-6,w):
        for j in range(0,h):
            if pixels[i+j*w] != 0:
                return True
    return False

def totext(img):
    """
    Returns the string contained in the image img
    """
    try:
        return subprocess.check_output([config.gocr, "-i", img], universal_newlines=True).strip()
    except FileNotFoundError:
        raise GocrNotInstalled()
