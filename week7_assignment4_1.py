import RPi.GPIO as GPIO
import time

SW = [0, 5, 6, 13, 19]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range(1,5):
    GPIO.setup(SW[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

swtime = [0, 1, 1, 1, 1]
swstatus = [0, 0, 0, 0, 0]
swValue = [0, 0, 0, 0, 0]
i = 1
try:
    while True:
        swValue[i] = GPIO.input(SW[i])
        if not swstatus[i]:
            if swValue[i]:
                swstatus[i] = 1
                print("('SW",i, " click', ", swtime[i], ")")
                swtime[i] += 1
        else:
            if swValue[i] == 0:
                swstatus[i] = 0
        i += 1
        if i == 5:
            i = 1
        
        time.sleep(0.03)

except KeyboardInterrupt:
    pass

GPIO.cleanup()