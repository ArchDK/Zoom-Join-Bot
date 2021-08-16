from os import getenv
import subprocess
import pyautogui
import time
from math import ceil
from datetime import datetime
import cWindow
from threading import Thread

class joinZoom():
    def __init__(self):
        self.zoomPath = getenv('APPDATA') + "\\Zoom\\bin\\Zoom.exe"#Zoom path
        self.cW = cWindow.cWindow()

    def openZoom(self,zoomTime,lists):
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now,"%H:%M:%S")
        diff = zoomTime - now
        time.sleep(ceil(diff.total_seconds()))
        subprocess.call(self.zoomPath)
        self.focusWindow(".*Zoom*.")
        time.sleep(3)
        self.clickBtn("Asset\joinBtn.jpg")
        time.sleep(3)
        self.enterMeetingID(lists[1].replace(" ",""))#ID
        time.sleep(6)
        self.enterPassword(lists[2])#Password
        time.sleep(3)

    def clickBtn(self, img):
        btn = None
        val = 1
        while btn==None:
            btn = pyautogui.locateCenterOnScreen(img, confidence=val)
            val -= 0.025
            print(val)
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
        now = now.strftime("%H:%M:%S")
        now = datetime.strptime(now,"%H:%M:%S")
        diff = endZoom - now
        time.sleep(ceil(diff.total_seconds()))
        self.focusWindow(".*Zoom Meeting*.")
        self.clickBtn("Asset\exitBtn.jpg")
        self.clickBtn("Asset\leaveMeeting.jpg")

    def focusWindow(self,wildcard):
        self.cW.findWindowName(wildcard)
        #self.cW.bringToTop() #Close because program keep crashing
        self.cW.setForegroundWindow()

    def main(self,lists):
        print(lists)
        thread = Thread(target=self.openZoom,args=(datetime.strptime(lists[3]+":00","%H:%M:%S"),lists,))
        thread.start()
        print("Is thread1 alive:", thread.is_alive())
        if(lists[4]!= ""):
            thread1 = Thread(target=self.leaveZoom,args=(datetime.strptime(lists[4]+":00","%H:%M:%S"),))
            thread1.start()
            print("Is thread1 alive:", thread1.is_alive())
