# coding=utf-8

from wx import *


class ConciseTextCtrl(TextCtrl):

    def __init__(self, parent, id=ID_ANY, value=EmptyString, height=2,
                 hint=EmptyString, style=0, name=TextCtrlNameStr):
        super(ConciseTextCtrl, self).__init__(parent=parent, id=id, value=value, style=style | BORDER_NONE, name=name)

        self.sizer = BoxSizer(VERTICAL)
        self.staticLine = StaticLine()

        self.focus = "BLUE"
        self.normal = "GREY"

        self.SetBackgroundColour(parent.GetBackgroundColour())
        self.SetHint(hint)

        self.staticLine = StaticLine(parent=parent)
        self.staticLine.SetBackgroundColour("BLUE")
        self.staticLine.SetForegroundColour("BLUE")

        self.sizer.Add(self, flag=EXPAND)
        self.sizer.Add(self.staticLine, flag=EXPAND | TOP, border=height)

        self.Bind(EVT_SET_FOCUS, handler=self.focusColour)
        self.Bind(EVT_KILL_FOCUS, handler=self.normalColour)

    def GetBoxSizer(self):
        return self.sizer

    def GetLineColour(self):
        return self.staticLine.GetBackgroundColour()

    def GetLineSize(self):
        return self.staticLine.GetSize()

    def SetLineColour(self, colour):
        result = self.staticLine.SetForegroundColour(colour)
        self.sizer.Layout()
        Yield()

        return result

    def SetLineSize(self, size):
        self.staticLine.SetSize(size)

    def FocusLine(self, normalColour, focusColour):
        self.normal = normalColour
        self.focus = focusColour

    def focusColour(self, event: Event):
        self.SetForegroundColour(self.focus)

        event.Skip()

    def normalColour(self, event: Event):
        self.SetForegroundColour(self.normal)

        event.Skip()
