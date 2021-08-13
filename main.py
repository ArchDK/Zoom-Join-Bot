import time
from datetime import datetime
import joinZoom

def main():
    zoom = joinZoom.joinZoom()
    zoom.openZoom(datetime(2021,8,12,13,0,0))#year,month,day,hour,min,sec
    zoom.clickBtn("Asset\joinBtn.jpg")
    time.sleep(3)
    zoom.enterMeetingID("873 225 7725")#ID
    time.sleep(3)
    zoom.enterPassword("123")#Password
    time.sleep(3)
    #zoom.leaveZoom(datetime(2021,8,12,11,3,10))#year,month,day,hour,min,sec

if __name__ == "__main__":
    main()


