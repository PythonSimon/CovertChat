# coding=utf-8

from re import *
from wx import *

from .Base import BaseFrame
from .ConciseTextCtrl import ConciseTextCtrl
from .MainPanel import MainPanelFrame
from .Register import RegisterFrame
from Client.Configure import *
from Client.Service.LoginService import login


class LoginFrame(BaseFrame):
    REGISTER = 11
    LOGIN = 12

    def __init__(self):
        super(LoginFrame, self).__init__(
            (350, 220),
            "秘信",
            r"Resource\MainIcon.png",
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | STAY_ON_TOP
        )

        self.registerFrame = RegisterFrame(self)

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        inputPanel = Panel(self.panel, style=BORDER_SIMPLE)

        inputSizer = BoxSizer(VERTICAL)

        defaultFont = Font(11, SCRIPT, NORMAL, NORMAL, False)
        emailCtrl = ConciseTextCtrl(inputPanel, hint="邮箱")
        passwordCtrl = ConciseTextCtrl(inputPanel, hint="密码", style=TE_PASSWORD)

        self.globals["email"] = emailCtrl
        self.globals["password"] = passwordCtrl

        emailCtrl.SetFont(defaultFont)
        emailCtrl.SetBackgroundColour(self.backgroundColor)
        emailCtrl.FocusLine("rgb(79, 79, 79)", "rgb(102, 147, 208)")
        passwordCtrl.SetFont(defaultFont)
        passwordCtrl.SetBackgroundColour(self.backgroundColor)
        passwordCtrl.FocusLine("rgb(111, 113, 113)", "rgb(102, 147, 208)")

        inputSizer.Add(emailCtrl.GetBoxSizer(), flag=ALIGN_CENTER | SHAPED | TOP | BOTTOM | RIGHT, border=10)
        inputSizer.Add(passwordCtrl.GetBoxSizer(), flag=ALIGN_CENTER | SHAPED | TOP | BOTTOM | RIGHT, border=10)

        inputPanel.SetSizer(inputSizer)

        inputPanel.Layout()

        buttonSizer = BoxSizer(HORIZONTAL)

        defaultFont = Font(12, SCRIPT, NORMAL, NORMAL, False)
        registerButton = Button(self.panel, id=LoginFrame.REGISTER, label="注册")
        loginButton = Button(self.panel, id=LoginFrame.LOGIN, label="登录")

        registerButton.SetFont(defaultFont)
        loginButton.SetFont(defaultFont)

        buttonSizer.Add(registerButton, flag=ALIGN_CENTER | SHAPED | RIGHT, border=15)
        buttonSizer.Add(loginButton, flag=ALIGN_CENTER | SHAPED | LEFT, border=15)

        sizer.Add(inputPanel, flag=EXPAND | ALL, border=20)
        sizer.Add(buttonSizer, flag=ALIGN_CENTER | SHAPED)

        self.panel.SetSizer(sizer)

        self.SetSize((0, 0))
        self.SetSize((350, 220))
        self.SetMinSize((350, 220))
        self.SetMaxSize((350, 220))
        self.panel.Layout()

        self.Bind(EVT_BUTTON, handler=self.register, id=LoginFrame.REGISTER)
        self.Bind(EVT_BUTTON, handler=self.login, id=LoginFrame.LOGIN)

    def register(self, event):
        if not self.registerFrame.IsShown():
            self.registerFrame.Show()

    def login(self, event):
        email = self.globals["email"].GetValue()
        password = self.globals["password"].GetValue()

        if (not search(r"^[^ ]+$", email)) or (not search(r"^[^ ]+$", password)):
            mistake = MessageDialog(None, "请完整填写信息！", caption="无法登录", style=OK | ICON_EXCLAMATION)
            mistake.ShowModal()
        else:
            result = login(email, password)

            if result["result"] == LoginResult.SUCCESS:
                del result["result"]

                self.Hide()

                MainPanelFrame(**result)
            elif result["result"] == LoginResult.USER_NONE:
                fail = MessageDialog(None, "用户不存在！", caption="登录失败", style=OK | ICON_ERROR)
                fail.ShowModal()
            elif result["result"] == LoginResult.PASSWORD_WRONG:
                fail = MessageDialog(None, "密码错误！", caption="登陆失败", style=OK | ICON_ERROR)
                fail.ShowModal()
            elif result["result"] == LoginResult.SERVER:
                fail = MessageDialog(None, "服务器连接异常", caption="连接失败", style=OK | ICON_ERROR)
                fail.ShowModal()
