# coding=utf-8

from wx import *

from Base import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__(
            (535, 420),
            "秘信",
            r"..\Resource\MainIcon",
            warn=False,
            backgroundColor="rgb(239,252,255)"
        )
