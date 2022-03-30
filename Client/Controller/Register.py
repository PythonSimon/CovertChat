# coding=utf-8

from wx import *

from .Base import *


class RegisterFrame(BaseFrame):

    def __init__(self, parent, email):
        super(RegisterFrame, self).__init__(
            (340, 530),
            "秘信",
            r"Resource\MainIcon.png",
            parent=parent,
            warn=False,
            backgroundColor="#F5F8F9",
            style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX | FRAME_FLOAT_ON_PARENT
        )

        self.main()

    def main(self):
        sizer = BoxSizer(VERTICAL)

        inputPanel = Panel(self.panel, style=BORDER_DOUBLE)

        inputSizer = FlexGridSizer(5, 2, vgap=15, hgap=10)

        inputPanel.SetSizer(inputSizer)

        inputPanel.Layout()

        sizer.Add(inputPanel, glag=EXPAND | ALL, border=20)

        self.panel.SetSizer(sizer)

        self.SetSize((0, 0))
        self.SetSize((340, 530))
        self.SetMinSize((340, 530))
        self.SetMaxSize((340, 530))
        self.panel.Layout()
