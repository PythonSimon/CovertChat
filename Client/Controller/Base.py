# coding=utf-8

import sys

from wx import *


class BaseFrame(Frame):

    def __init__(self, size, title, icon, warn=True, closingWarning="确认关闭？", parent=None, waveSize=(-1, -1),
                 window="default", backgroundColor="GREY", style=DEFAULT_FRAME_STYLE ^ MAXIMIZE_BOX):
        super(BaseFrame, self).__init__(parent=parent, title=title, size=size, style=style)

        self.globals = {}

        self.size = size
        self.title = title
        self.icon = icon
        self.warn = warn
        self.closingWarning = closingWarning
        self.parent = parent
        self.waveSize = waveSize
        self.window = window
        self.backgroundColor = backgroundColor
        self.style = style

        if window == "default":
            self.panel = Panel(parent=self)
        elif window == "split-v":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.leftPanel = Panel(self.splitter)
            self.rightPanel = Panel(self.splitter)
            self.splitter.SplitVertically(self.leftPanel, self.rightPanel, self.GetSize()[0] / 2)
            self.splitter.SetMinimumPaneSize(self.GetSize()[0] / 10)
        elif window == "split-h":
            self.splitter = SplitterWindow(self, style=SP_3DSASH)
            self.topPanel = Panel(self.splitter)
            self.bottomPanel = Panel(self.splitter)
            self.splitter.SplitHorizontally(self.topPanel, self.bottomPanel, self.GetSize()[1] / 2)
            self.splitter.SetMinimumPaneSize(self.GetSize()[1] / 10)

        icon = Icon(icon, BITMAP_TYPE_PNG)

        self.Center()
        self.SetBackgroundColour(backgroundColor)
        self.SetIcon(icon)

        if -1 not in waveSize:
            self.SetMinSize((size[0] - waveSize[0], size[1] - waveSize[1]))
            self.SetMaxSize((size[0] + waveSize[0], size[1] + waveSize[1]))

        self.Bind(EVT_CLOSE, self.onClose)

    def onClose(self, event):
        if self.warn:
            warnMd = MessageDialog(None, self.closingWarning, caption="提示", style=YES_NO | ICON_EXCLAMATION)

            if warnMd.ShowModal() == ID_YES:
                self.Destroy()
                sys.exit(0)
            else:
                warnMd.Destroy()
        else:
            self.Destroy()
            sys.exit(0)

    def close(self, event=None):
        self.Destroy()
        sys.exit(0)
