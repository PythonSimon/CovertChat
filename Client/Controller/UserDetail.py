# coding=utf-8

from wx import *

from .Base import BaseFrame


class UserDetailFrame(BaseFrame):

    def __init__(self, parent, uid, email, name, pattern, password, *password2):
        super(UserDetailFrame, self).__init__(
            (400, 400),
            "秘信",
            r"..\Resource\MainIcon.png",
            parent=parent,
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | FRAME_FLOAT_ON_PARENT
        )
