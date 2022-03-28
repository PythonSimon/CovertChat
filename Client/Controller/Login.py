# coding=utf-8

from wx import *

from .Base import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__(
            (455, 340),
            "秘信",
            r"Resource\MainIcon.png",
            warn=False,
            backgroundColor="rgb(239,252,255)",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | STAY_ON_TOP
        )

        self.main()

    def main(self):
        topImageBitmap = Bitmap(r"Resource\LoginTop.png", BITMAP_TYPE_PNG)
        topImage = StaticBitmap(self.panel, bitmap=topImageBitmap)
