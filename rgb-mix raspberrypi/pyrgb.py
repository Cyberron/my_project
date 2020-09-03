import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
pwmR = GPIO.PWM(16, 1000)
pwmR.start(0)

GPIO.setup(20, GPIO.OUT)
pwmG = GPIO.PWM(20, 1000)
pwmG.start(0)

GPIO.setup(21, GPIO.OUT)
pwmB = GPIO.PWM(21, 1000)
pwmB.start(0)


def color(pr, pg, pb, r, g, b):
    def cvt(v):
        return v * 100 / 256

    pr.ChangeDutyCycle(cvt(r))
    pg.ChangeDutyCycle(cvt(g))
    pb.ChangeDutyCycle(cvt(b))


try:
    while True:
        color(pwmR, pwmG, pwmB, 255, 0, 0)  # Red
        time.sleep(1)
        color(pwmR, pwmG, pwmB, 0, 255, 0)  # Green
        time.sleep(1)
        color(pwmR, pwmG, pwmB, 0, 0, 255)  # Blue
        time.sleep(1)
        color(pwmR, pwmG, pwmB, 255, 255, 255)  # White
        time.sleep(1)
        color(pwmR, pwmG, pwmB, 255, 204, 0)  # yellow
        time.sleep(1)
        color(pwmR, pwmG, pwmB, 255, 0, 255)  # purple
        time.sleep(1)

except KeyboardInterrupt:  # Ctrl + C
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()
    GPIO.cleanup()
    print("Exit")
