# coding=utf-8

from re import *
from wx import *

from .Base import BaseFrame
from .Register import RegisterFrame
from Client.Configure import *
from Client.Service.LoginService import login

REGISTER = 11
LOGIN = 12


class LoginFrame(BaseFrame):

    def __init__(self):
        super(LoginFrame, self).__init__(
            (350, 220),
            "秘信",
            r"Resource\MainIcon.png",
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | STAY_ON_TOP
        )

        self.registering = False

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        inputPanel = Panel(self.panel, style=BORDER_DOUBLE)

        inputSizer = FlexGridSizer(2, 2, vgap=0, hgap=10)

        inputSizer.AddGrowableRow(0, 1)
        inputSizer.AddGrowableRow(1, 1)
        inputSizer.AddGrowableCol(0, 1)
        inputSizer.AddGrowableCol(1, 2)

        defaultFont = Font(10, SCRIPT, NORMAL, NORMAL, False)
        emailText = StaticText(inputPanel, label="邮箱")
        emailCtrl = TextCtrl(inputPanel)
        passwordText = StaticText(inputPanel, label="密码")
        passwordCtrl = TextCtrl(inputPanel, style=TE_PASSWORD)

        self.globals["email"] = emailCtrl
        self.globals["password"] = passwordCtrl

        emailText.SetFont(defaultFont)
        emailCtrl.SetFont(defaultFont)
        passwordText.SetFont(defaultFont)
        passwordCtrl.SetFont(defaultFont)

        inputSizer.Add(emailText, flag=ALIGN_CENTER)
        inputSizer.Add(emailCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(passwordText, flag=ALIGN_CENTER)
        inputSizer.Add(passwordCtrl, flag=SHAPED | ALL, border=10)

        inputPanel.SetSizer(inputSizer)

        inputPanel.Layout()

        buttonSizer = BoxSizer(HORIZONTAL)

        defaultFont = Font(12, SCRIPT, NORMAL, NORMAL, False)
        registerButton = Button(self.panel, id=REGISTER, label="注册")
        loginButton = Button(self.panel, id=LOGIN, label="登录")

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

        self.Bind(EVT_BUTTON, handler=self.register, id=REGISTER)
        self.Bind(EVT_BUTTON, handler=self.login, id=LOGIN)

    def register(self, event):
        if not self.registering:
            RegisterFrame(
                self,
                self.globals["email"].GetValue()
            ).Show()
            self.registering = True

    def login(self, event):
        email = self.globals["email"].GetValue()
        password = self.globals["password"].GetVaalue()

        if (not search(r"^[^ ]+$", email)) or (not search(r"^[^ ]+$", password)):
            mistake = MessageDialog(None, "请完整填写信息！", caption="无法登录", style=OK | ICON_EXCLAMATION)
            mistake.ShowModal()
        else:
            result = login(email, password)

            if result["result"] == LoginResult.SUCCESS:
                pass
            elif result["result"] == LoginResult.USER_NONE:
                fail = MessageDialog(None, "用户不存在！", caption="登录失败", style=OK | ICON_ERROR)
                fail.ShowModal()
            elif result["result"] == LoginResult.PASSWORD_WRONG:
                fail = MessageDialog(None, "密码错误！", caption="登陆失败", style=OK | ICON_ERROR)
                fail.ShowModal()
