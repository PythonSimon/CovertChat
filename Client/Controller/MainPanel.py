# coding=utf-8

from wx import *
from wx.lib.buttons import *

from Base import BaseFrame
from Client.Configure import *


class MainPanelFrame(BaseFrame):

    def __init__(self, uid, email, status, name, password, password2, friends: list[str], avatar):
        super(MainPanelFrame, self).__init__(
            (350, 1200),
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

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        userPanel = Panel(self.panel)

        userSizer = BoxSizer(HORIZONTAL)

        avatarBitmap = Bitmap(f"Client\\Resource\\Avatar{self.avatar}.png", BITMAP_TYPE_PNG)
        avatar = BitmapButton(self.panel, bitmap=avatarBitmap)
        name = StaticText(userPanel, label=self.name)

        userSizer.Add(avatar, flag=ALIGN_LEFT | ALIGN_CENTER_HORIZONTAL | LEFT, border=20)
        userSizer.Add(name, flag=ALIGN_CENTER_HORIZONTAL | LEFT, border=25)

        userPanel.SetSizer(userSizer)

        sizer.Add(userPanel, flag=EXPAND)

        self.panel.SetSizer(sizer)

        self.panel.Layout()


class MainApp(App):

    def OnInit(self):
        mainFrame = MainPanelFrame("1", "81@qq.com", "f", "程序喵", "12", "21", [""], "2")
        mainFrame.Show()

        return True

    def OnExit(self):
        return 0


if __name__ == "__main__":
    mainApp = MainApp()

    mainApp.MainLoop()
