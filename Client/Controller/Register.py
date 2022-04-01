# coding=utf-8

from wx import *

from .Base import BaseFrame

GET_CODE = 1
REGISTER = 2


class RegisterFrame(BaseFrame):

    def __init__(self, parent, email):
        super(RegisterFrame, self).__init__(
            (340, 475),
            "秘信",
            r"Resource\MainIcon.png",
            parent=parent,
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | FRAME_FLOAT_ON_PARENT
        )

        self.email = email

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        titleText = StaticText(self.panel, label="注册")

        titleText.SetFont(Font(15, SCRIPT, NORMAL, BOLD, False))

        inputPanel = Panel(self.panel, style=BORDER_DOUBLE)

        inputSizer = FlexGridSizer(5, 2, vgap=15, hgap=10)

        inputSizer.AddGrowableRow(0, 1)
        inputSizer.AddGrowableRow(1, 1)
        inputSizer.AddGrowableRow(2, 1)
        inputSizer.AddGrowableRow(3, 1)
        inputSizer.AddGrowableRow(4, 1)
        inputSizer.AddGrowableCol(0, 1)
        inputSizer.AddGrowableCol(1, 2)

        defaultFont = Font(10, SCRIPT, NORMAL, NORMAL, False)
        nameText = StaticText(inputPanel, label="昵称")
        nameCtrl = TextCtrl(inputPanel)
        passwordText = StaticText(inputPanel, label="密码")
        passwordCtrl = TextCtrl(inputPanel)
        password2Text = StaticText(inputPanel, label="备用密码")
        password2Ctrl = TextCtrl(inputPanel)
        emailText = StaticText(inputPanel, label="QQ邮箱")
        emailCtrl = TextCtrl(inputPanel)
        codeText = StaticText(inputPanel, label="验证码")
        codeCtrl = TextCtrl(inputPanel)

        self.globals["name"] = nameCtrl
        self.globals["password"] = passwordCtrl
        self.globals["password2"] = password2Ctrl
        self.globals["email"] = emailCtrl
        self.globals["code"] = codeCtrl

        nameText.SetFont(defaultFont)
        nameCtrl.SetFont(defaultFont)
        passwordText.SetFont(defaultFont)
        passwordCtrl.SetFont(defaultFont)
        password2Text.SetFont(defaultFont)
        password2Ctrl.SetFont(defaultFont)
        emailText.SetFont(defaultFont)
        emailCtrl.SetFont(defaultFont)
        emailCtrl.SetValue(self.email)
        codeText.SetFont(defaultFont)
        codeCtrl.SetFont(defaultFont)

        inputSizer.Add(nameText, flag=ALIGN_CENTER)
        inputSizer.Add(nameCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(passwordText, flag=ALIGN_CENTER)
        inputSizer.Add(passwordCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(password2Text, flag=ALIGN_CENTER)
        inputSizer.Add(password2Ctrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(emailText, flag=ALIGN_CENTER)
        inputSizer.Add(emailCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(codeText, flag=ALIGN_CENTER)
        inputSizer.Add(codeCtrl, flag=SHAPED | ALL, border=10)

        inputPanel.SetSizer(inputSizer)

        inputPanel.Layout()

        buttonSizer = BoxSizer(HORIZONTAL)

        getCodeButton = Button(self.panel, label="获取验证码")
        registerButton = Button(self.panel, label="注册")

        buttonSizer.Add(getCodeButton, id=GET_CODE, flag=RIGHT, border=15)
        buttonSizer.Add(registerButton, id=REGISTER, flag=LEFT, border=15)

        sizer.Add(titleText, flag=ALIGN_CENTER | ALL, border=10)
        sizer.Add(inputPanel, flag=EXPAND | ALL, border=20)
        sizer.Add(buttonSizer, flag=ALIGN_CENTER)

        self.panel.SetSizer(sizer)

        self.SetSize((0, 0))
        self.SetSize(self.size)
        self.SetMinSize(self.size)
        self.SetMaxSize(self.size)
        self.panel.Layout()

        self.Bind(EVT_BUTTON, handler=self.getCode, id=GET_CODE)
        self.Bind(EVT_BUTTON, handler=self.register, id=REGISTER)

    def getCode(self, event):
        pass

    def register(self, event):
        name = self.globals["name"].GetValue()
        password = self.globals["password"].GetValue()
        password2 = self.globals["password2"].GetValue()
        email = self.globals["email"].GetValue()
        code = self.globals["code"].GetValue()

        pass

    def onClose(self, event):
        self.Hide()
