# coding=utf-8

from re import *
from threading import *
from time import *
from wx import *
from wx.lib.agw.hyperlink import *

from .Base import BaseFrame
from Client.Configure import *
from Client.Service.RegisterService import sendCode, register

GET_CODE = 21
REGISTER = 22


class RegisterFrame(BaseFrame):

    def __init__(self, parent: BaseFrame, email):
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
        self.oneMinute = False

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
        getCode = HyperLinkCtrl(inputPanel, id=GET_CODE, label="获取验证码")
        codeCtrl = TextCtrl(inputPanel)

        self.globals["name"] = nameCtrl
        self.globals["password"] = passwordCtrl
        self.globals["password2"] = password2Ctrl
        self.globals["email"] = emailCtrl
        self.globals["code"] = codeCtrl
        self.globals["getCode"] = getCode

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
        getCode.SetForegroundColour("#5C686C")
        getCode.AutoBrowse(False)
        getCode.OpenInSameWindow(True)
        getCode.SetToolTip(ToolTip(""))
        codeCtrl.SetFont(defaultFont)

        inputSizer.Add(nameText, flag=ALIGN_CENTER)
        inputSizer.Add(nameCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(passwordText, flag=ALIGN_CENTER)
        inputSizer.Add(passwordCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(password2Text, flag=ALIGN_CENTER)
        inputSizer.Add(password2Ctrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(emailText, flag=ALIGN_CENTER)
        inputSizer.Add(emailCtrl, flag=SHAPED | ALL, border=10)
        inputSizer.Add(getCode, flag=ALIGN_CENTER)
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

        self.Bind(EVT_HYPERLINK_LEFT, handler=self.getCode, id=GET_CODE)
        self.Bind(EVT_BUTTON, handler=self.register, id=REGISTER)
        Thread(target=self.wait).start()

    def getCode(self, event):
        if not self.oneMinute:
            email = self.globals["email"].GetValue()

            if search(r"^\w+@\w+\.\w+$", email):
                self.code = sendCode(email)

                if self.code == RegisterResult.SEND_CODE_FAIL:
                    faiLed = MessageDialog(None, "验证码发送失败，请检查邮箱及网络情况！", caption="发送失败", style=OK | ICON_ERROR)
                    faiLed.ShowModal()
                else:
                    self.oneMinute = True
            else:
                mistake = MessageDialog(None, "邮箱填写有误！", caption="无法发送", style=OK | ICON_ERROR)
                mistake.ShowModal()

    def register(self, event):
        self.parent.Show()
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

        if not search(r"^\w+@\w+\.\w+$", email, flags=ASCII):
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
            mistake.ShowModal()
        else:
            result = register(email, name, password, password2)

            if result == RegisterResult.SUCCESS:
                success = MessageDialog(None, "注册成功！", caption="注册成功", style=OK | ICON_INFORMATION)
                success.ShowModal()

                self.Hide()
                self.parent.Show()
            elif result == RegisterResult.USER_EXIST:
                fail = MessageDialog(None, "邮箱已注册", caption="注册失败", style=OK | ICON_ERROR)
                fail.ShowModal()
            elif result == RegisterResult.SERVER:
                fail = MessageDialog(None, "服务器连接异常", caption="连接失败", style=OK | ICON_ERROR)
                fail.ShowModal()

    def wait(self):
        while True:
            if self.oneMinute:
                for rest in range(60, 0, -1):
                    self.globals["getCode"].SetLabel(f"{rest}秒后可重发")
                    self.globals["getCode"].SetFont(Font(9, SCRIPT, NORMAL, NORMAL, False))
                    sleep(1)

                self.globals["getCode"].SetLabel("获取验证码")
                self.globals["getCode"].SetFont(Font(10, SCRIPT, NORMAL, NORMAL, False))

                self.oneMinute = False

            sleep(1)

    def onClose(self, event):
        self.Hide()
