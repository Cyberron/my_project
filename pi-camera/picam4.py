# pi cam 4 take video
from picamera import PiCamera, Color
import time

from time import sleep
from datetime import datetime
from datetime import timedelta

camera = PiCamera()

print("On video process....")

camera.rotation = 0  # 0-360
camera.resolution = (1024,600) # or 1920 x 1080,2592 x 1944 ,etc.
camera.framerate = 15
camera.brightness = 50  # 0-100 , 50=default
camera.annotate_text_size = 32 # text size 6-160 , 32=default
camera.annotate_text = "Hello world!" # fill text in pic
camera.start_preview(alpha=255)  # alpha is 0 to 255

nt = datetime.now()

camera.start_recording('/home/pi/Videos/video{:d}.{:d}.{:d}.{:d}.{:d}.{:d}.h264' \
                       .format(nt.year,nt.month,nt.day,nt.hour,nt.minute,nt.second))     # video
sleep(10)
camera.stop_recording()

print("Finish !")
camera.stop_preview()