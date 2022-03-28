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
            backgroundColor="rgb(239,252,255)"
        )

        self.main()

    def main(self):
        pass
