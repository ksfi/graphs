#!/usr/bin/env python3

import PIL
import cv2 as cv

class Image:
    def __init__(self, path):
        self.img = Image.open(path)

    def recup(self):
        pass
