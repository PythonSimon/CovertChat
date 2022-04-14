# coding=utf-8

from wx import *
from wx.lib.buttons import *

from .Base import BaseFrame
from Client.Configure import *


class MainPanelFrame(BaseFrame):

    def __init__(self, uid, email, status, name, password, password2, friends: list, avatar):
        super(MainPanelFrame, self).__init__(
            (350 , 220),
            "秘信",
            r"Resource\MainIcon.png",
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | STAY_ON_TOP
        )

        self.uid = uid
        self.email = email
        self.status = status
        self.name = name
        self.password = password
        self.password2 = password2
        self.friends = friends
        self.avatar = avatar
