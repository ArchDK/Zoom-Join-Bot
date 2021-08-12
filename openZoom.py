import time
from datetime import datetime
import joinZoom

def main():
    zoom = joinZoom.joinClass()
    zoom.openZoom(datetime(2021,8,12,10,59,10))
    zoom.clickBtn("Asset\joinBtn.jpg")
    time.sleep(3)
    zoom.enterMeetingID("5047292266")
    time.sleep(3)
    zoom.enterPassword("123")
    time.sleep(7)
    zoom.leaveZoom(datetime(2021,8,12,11,3,10))

main()


