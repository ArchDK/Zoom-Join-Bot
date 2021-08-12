import re
import win32gui, win32com.client

class cWindow:
    def __init__(self):
        self.hwnd = None
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def bringToTop(self):
        win32gui.BringWindowToTop(self.hwnd)

    def setForegroundWindow(self):
        self.shell.SendKeys('%')
        win32gui.SetForegroundWindow(self.hwnd)

    def windowEnum(self, hwnd, name):
        if re.match(name, str(win32gui.GetWindowText(hwnd))) != None:
            self.hwnd = hwnd

    def findWindowName(self, name):
        self.hwnd = None
        win32gui.EnumWindows(self.windowEnum, name)