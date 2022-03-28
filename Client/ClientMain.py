# coding=utf-8

from wx import *

from Controller.Login import LoginFrame


class MainApp(App):

    def OnInit(self):
        mainFrame = LoginFrame()
        mainFrame.Show()

        return True

    def OnExit(self):
        return 0


if __name__ == "__main__":
    mainApp = MainApp()

    mainApp.MainLoop()
