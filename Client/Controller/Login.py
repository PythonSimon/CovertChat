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
            waveSize=(0, 0),
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | STAY_ON_TOP
        )

        self.main()

    def main(self):
        pass
