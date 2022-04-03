# coding=utf-8

from re import *
from wx import *

from .Base import BaseFrame
from Client.Service.RegisterService import sendCode

GET_CODE = 21
REGISTER = 22


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
        self.code = ""

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        titleText = StaticText(self.panel, label="注册")

        titleText.SetFont(Font(15, SCRIPT, NORMAL, BOLD, False))

        inputPanel = Panel(self.panel, style=BORDER_DOUBLE)

        self.globals["inputPanel"] = inputPanel

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
        emailText = StaticText(inputPanel, label="邮箱")
        emailCtrl = TextCtrl(inputPanel)
        getCode = Button(inputPanel, id=GET_CODE, label="获取验证码", style=BORDER_NONE)
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
        getCode.SetFont(defaultFont)
        getCode.SetForegroundColour("BLUE")
        getCode.SetBackgroundColour(self.backgroundColor)
        codeCtrl.SetFont(defaultFont)

        inputSizer.Add(nameText, flag=ALIGN_CENTER)
        inputSizer.Add(nameCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(passwordText, flag=ALIGN_CENTER)
        inputSizer.Add(passwordCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(password2Text, flag=ALIGN_CENTER)
        inputSizer.Add(password2Ctrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(emailText, flag=ALIGN_CENTER)
        inputSizer.Add(emailCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(getCode, flag=ALIGN_TOP | ALIGN_CENTER_HORIZONTAL | TOP, border=7)
        inputSizer.Add(codeCtrl, flag=SHAPED | ALL, border=10)

        inputPanel.SetSizer(inputSizer)

        inputPanel.Layout()

        registerButton = Button(self.panel, id=REGISTER, label="注册")

        sizer.Add(titleText, flag=ALIGN_CENTER | ALL, border=10)
        sizer.Add(inputPanel, flag=EXPAND | ALL, border=20)
        sizer.Add(registerButton, flag=EXPAND | LEFT | RIGHT | BOTTOM, border=25)

        self.panel.SetSizer(sizer)

        self.SetSize((0, 0))
        self.SetSize(self.size)
        self.SetMinSize(self.size)
        self.SetMaxSize(self.size)
        self.panel.Layout()

        self.Bind(EVT_BUTTON, handler=self.getCode, id=GET_CODE)
        self.Bind(EVT_BUTTON, handler=self.register, id=REGISTER)

    def getCode(self, event):
        email = self.globals["email"].GetValue()

        if search(r"^\w+@.+\..+$", email):
            self.code = sendCode(email)

            if self.code == -1:
                faiLed = MessageDialog(None, "验证码发送失败，请检查邮箱及网络情况！", caption="发送失败", style=OK | ICON_ERROR)
                faiLed.ShowModal()
        else:
            mistake = MessageDialog(None, "邮箱填写有误！", caption="无法发送", style=OK | ICON_ERROR)
            mistake.ShowModal()

    def register(self, event):
        inputPanel = self.globals["inputPanel"]
        name = self.globals["name"].GetValue()
        password = self.globals["password"].GetValue()
        password2 = self.globals["password2"].GetValue()
        email = self.globals["email"].GetValue()
        code = self.globals["code"].GetValue()

        mistake = False

        if not search(r"^[^ ]+$", name):
            self.globals["name"].SetBackgroundColour("PINK")
            self.globals["name"].SetFocus()

            inputPanel.Layout()

            mistake = True
        else:
            self.globals["name"].SetBackgroundColour("WHITE")

            inputPanel.Layout()

        if not search(r"^\w+$", password, flags=ASCII):
            self.globals["password"].SetBackgroundColour("PINK")
            self.globals["password"].SetFocus()

            inputPanel.Layout()

            mistake = True
        else:
            self.globals["password"].SetBackgroundColour("WHITE")

            inputPanel.Layout()

        if not search(r"^\w+$", password2, flags=ASCII):
            self.globals["password2"].SetBackgroundColour("PINK")
            self.globals["password2"].SetFocus()

            inputPanel.Layout()

            mistake = True
        else:
            self.globals["password2"].SetBackgroundColour("WHITE")

            inputPanel.Layout()

        if not search(r"^\w+@.+\..+$", email, flags=ASCII):
            self.globals["email"].SetBackgroundColour("PINK")
            self.globals["email"].SetFocus()

            inputPanel.Layout()

            mistake = True
        else:
            self.globals["email"].SetBackgroundColour("WHITE")

            inputPanel.Layout()

        if self.code in ("", -1) or code != self.code:
            self.globals["code"].SetBackgroundColour("PINK")
            self.globals["code"].SetFocus()

            inputPanel.Layout()

            mistake = True
        else:
            self.globals["code"].SetBackgroundColour("WHITE")

            inputPanel.Layout()

        if mistake:
            mistake = MessageDialog(None, "信息填写有误，请根据红色指示改正！", caption="无法注册", style=OK | ICON_ERROR)

    def onClose(self, event):
        self.Hide()
