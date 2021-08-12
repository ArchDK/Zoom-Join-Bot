from os import getenv
import subprocess
import pyautogui
import time
from math import ceil
from datetime import datetime
import cWindow

class joinClass():
    def __init__(self):
        self.zoomPath = getenv('APPDATA') + "\\Zoom\\bin\\Zoom.exe"#Zoom path
        self.cW = cWindow.cWindow()

    def openZoom(self,zoomTime):
        now = datetime.now()
        diff = zoomTime - now
        time.sleep(ceil(diff.total_seconds()))
        subprocess.call(self.zoomPath)
        self.focusWindow(".*Zoom*.")
        time.sleep(5)

    def clickBtn(self, img):
        btn = None
        val = 1
        while btn==None:
            btn = pyautogui.locateCenterOnScreen(img, confidence=val)
            val -= 0.025
        pyautogui.moveTo(btn)
        pyautogui.click()
    
    def enterMeetingID(self, id):
        self.clickBtn("Asset\enterMeetingID.jpg")
        pyautogui.write(id)
        self.clickBtn("Asset\join.jpg")

    def enterPassword(self, password):
        self.clickBtn("Asset\meetingPassword.jpg")
        pyautogui.write(password)
        self.clickBtn("Asset\joinMeeting.jpg")

    def leaveZoom(self, endZoom):
        now = datetime.now()
        diff = endZoom - now
        time.sleep(ceil(diff.total_seconds()))
        self.focusWindow(".*Zoom Meeting*.")
        self.clickBtn("Asset\exitBtn.jpg")
        self.clickBtn("Asset\leaveMeeting.jpg")

    def focusWindow(self,wildcard):
        self.cW.findWindowName(wildcard)
        self.cW.bringToTop()
        self.cW.setForegroundWindow()
