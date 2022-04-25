# coding=utf-8

from wx import *
from wx.lib.buttons import *
from wx.lib.scrolledpanel import *

from Base import BaseFrame
from Client.Configure import *
from UserDetail import UserDetailFrame


class MainPanelFrame(BaseFrame):
    USER_DETAIL = 31

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
        avatar = BitmapButton(userPanel, id=MainPanelFrame.USER_DETAIL, bitmap=avatarBitmap, style=BORDER_NONE)
        name = StaticText(userPanel, label=self.name)

        avatar.SetToolTip(self.name)
        name.SetFont(Font(14, SCRIPT, NORMAL, NORMAL, False))

        userSizer.Add(avatar, flag=ALIGN_CENTER_VERTICAL | LEFT, border=20)
        userSizer.Add(name, flag=ALIGN_CENTER_VERTICAL | LEFT, border=25)

        userPanel.SetSizer(userSizer)

        friendsPanel = ScrolledPanel(self.panel, style=BORDER_SIMPLE)

        friendsSizer = BoxSizer(VERTICAL)

        for index, friend in enumerate(self.friends):
            friendAvatar = Bitmap(f"..\\Resource\\Avatar{friend['avatar']}.png.", BITMAP_TYPE_PNG)
            friendAvatar = Bitmap(friendAvatar.ConvertToImage().Scale(50, 50, wx.IMAGE_QUALITY_HIGH))
            friendName = friend["name"]
            friendButton = GenBitmapTextButton(friendsPanel, id=index, bitmap=friendAvatar, label=friendName,
                                               style=BORDER_NONE)
            # friendButton.SetBackgroundColour(self.backgroundColor)

            friendButton.SetFont(Font(14, SCRIPT, NORMAL, NORMAL, False))

            friendsSizer.Add(friendButton, flag=EXPAND)

            friendButton.Bind(EVT_BUTTON, self.chat)

        friendsPanel.SetSizer(friendsSizer)

        sizer.Add(userPanel, flag=UP, border=10)
        sizer.Add(friendsPanel, flag=EXPAND | UP, border=20)

        self.panel.SetSizer(sizer)

        self.panel.Layout()

        self.Bind(EVT_BUTTON, handler=self.userDetail, id=MainPanelFrame.USER_DETAIL)

    def userDetail(self, event):
        password = PasswordEntryDialog(self, "请输入用户密码", caption="身份验证")
        password.ShowModal()

        password = password.GetValue()

        if password == self.password:
            if self.status == Status.MAIN_USER:
                pass
            elif self.status == Status.SPECIAL_USER:
                mistake = MessageDialog(None, "密码错误！", caption="无法查看信息", style=OK | ICON_EXCLAMATION)
                mistake.ShowModal()
        elif password == self.password2:
            pass

    def chat(self, event):
        pass


class MainApp(App): 

    def OnInit(self):
        mainFrame = MainPanelFrame("1", "81@qq.com", Status.SPECIAL_USER, "程序喵", "12", "21", [{"avatar": "1", "name": "fr"}], "36")
        mainFrame.Show()

        return True

    def OnExit(self):
        return 0


if __name__ == "__main__":
    mainApp = MainApp()

    mainApp.MainLoop()
