# coding=utf-8

from wx import *

from .Base import *


class RegisterFrame(BaseFrame):

    def __init__(self, parent, email):
        super(RegisterFrame, self).__init__(
            (340, 530),
            "秘信",
            r"Resource\MainIcon.png",
            parent=parent,
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | FRAME_FLOAT_ON_PARENT
        )
