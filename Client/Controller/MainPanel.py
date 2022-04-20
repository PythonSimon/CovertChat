# coding=utf-8

from wx import *
from wx.lib.buttons import *
from wx.lib.scrolledpanel import *

from Base import BaseFrame
from Client.Configure import *


class MainPanelFrame(BaseFrame):

    def __init__(self, uid, email, status: Status, name, password, password2, friends: list[dict], avatar):
        super(MainPanelFrame, self).__init__(
            (350, 850),
            "秘信",
            r"..\Resource\MainIcon.png",
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

        avatarBitmap = Bitmap(f"..\\Resource\\Avatar{self.avatar}.png", BITMAP_TYPE_PNG)
        avatarBitmap = Bitmap(avatarBitmap.ConvertToImage().Scale(50, 50, wx.IMAGE_QUALITY_HIGH))
        avatar = BitmapButton(userPanel, bitmap=avatarBitmap)
        name = StaticText(userPanel, label=self.name)
        name.SetFont(Font(14, SCRIPT, NORMAL, NORMAL, False))

        userSizer.Add(avatar, flag=ALIGN_CENTER_VERTICAL | LEFT, border=20)
        userSizer.Add(name, flag=ALIGN_CENTER_VERTICAL | LEFT, border=25)

        userPanel.SetSizer(userSizer)

        friendsPanel = ScrolledPanel(self.panel, style=BORDER_SIMPLE)

        friendsSizer = FlexGridSizer(1, len(self.friends), 0, 1)

        for index, friend in enumerate(self.friends):
            friendAvatar = Bitmap(f"..\\Resource\\Avatar{friend['avatar']}.png.", BITMAP_TYPE_PNG)
            friendName = friend["name"]
            friendButton = GenBitmapTextButton(friendsPanel, id=index, bitmap=friendAvatar, label=friendName)

            friendButton.Bind(EVT_BUTTON, self.chat)

        friendsPanel.SetSizer(friendsSizer)

        sizer.Add(userPanel)
        sizer.Add(friendsPanel, flag=UP, border=20)

        self.panel.SetSizer(sizer)

        self.panel.Layout()

    def chat(self, event):
        pass


class MainApp(App): 

    def OnInit(self):
        mainFrame = MainPanelFrame("1", "81@qq.com", Status.MAIN_USER, "程序喵", "12", "21", [{"avatar": "1", "name": "fr"}], "36")
        mainFrame.Show()

        return True

    def OnExit(self):
        return 0


if __name__ == "__main__":
    mainApp = MainApp()

    mainApp.MainLoop()
