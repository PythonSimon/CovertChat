# coding=utf-8

from wx import *

from .Base import BaseFrame

REGISTER = 1
LOGIN = 2


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

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        inputPanel = Panel(self.panel, style=BORDER_DOUBLE)

        inputSizer = FlexGridSizer(2, 2, vgap=0, hgap=10)

        inputSizer.AddGrowableRow(0, 1)
        inputSizer.AddGrowableRow(1, 1)
        inputSizer.AddGrowableCol(0, 1)
        inputSizer.AddGrowableCol(1, 2)

        defaultFont = Font(Font(10, SCRIPT, NORMAL, NORMAL, False))
        emailText = StaticText(inputPanel, label="邮箱")
        emailCtrl = TextCtrl(inputPanel)
        passwordText = StaticText(inputPanel, label="密码")
        passwordCtrl = TextCtrl(inputPanel)

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

        defaultFont = Font(Font(12, SCRIPT, NORMAL, NORMAL, False))
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
