# coding=utf-8

from wx import *


class ConciseTextCtrl(TextCtrl):

    def __init__(self, parent, id=ID_ANY, value=EmptyString, height=2,
                 hint=EmptyString, style=0, name=TextCtrlNameStr):
        super(ConciseTextCtrl, self).__init__(parent=parent, id=id, value=value, style=style | BORDER_NONE, name=name)

        self.sizer = BoxSizer(VERTICAL)
        self.staticLine = StaticLine()

        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.SetHint(hint)

        self.staticLine = StaticLine(parent=parent)

        self.sizer.Add(self, flag=EXPAND)
        self.sizer.Add(self.staticLine, flag=EXPAND | TOP, border=height)

    def GetBoxSizer(self):
        return self.sizer

    def GetLineColour(self):
        return self.staticLine.GetBackgroundColour()

    def GetLineHeight(self):
        return self.staticLine.GetSize()[1]

    def SetLineColour(self, colour):
        return self.staticLine.SetBackgroundColour(colour)

    def SetLineHeight(self, height):
        self.staticLine.SetSize(
            Size(
                self.staticLine.GetSize()[0],
                height
            )
        )
