import time
from datetime import datetime
import joinZoom

def main():
    zoom = joinZoom.joinClass()
    zoom.openZoom(datetime(2021,8,12,10,59,10))#year,month,day,hour,min,sec
    zoom.clickBtn("Asset\joinBtn.jpg")
    time.sleep(3)
    zoom.enterMeetingID("")#ID
    time.sleep(3)
    zoom.enterPassword("")#Password
    time.sleep(3)
    zoom.leaveZoom(datetime(2021,8,12,11,3,10))#year,month,day,hour,min,sec

if __name__ == "__main__":
    main()


