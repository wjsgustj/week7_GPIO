import RPi.GPIO as GPIO
import time

SW = [0, 5, 6, 13, 19]
BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for i in range(1, 5):
    GPIO.setup(SW[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

swValue = [0, 0, 0, 0, 0]
swstatus = 0

doremi = [0, 262, 294, 330, 349, 392, 440, 494, 523]

try:
    while True:
        swstatus = 0
        for i in range(1, 5):
            swValue[i] = GPIO.input(SW[i])
            swstatus *= 10
            swstatus += swValue[i]
            time.sleep(0.03)
        
        if swstatus == 1000:
            p = GPIO.PWM(BUZZER, doremi[1])
        elif swstatus == 100:
            p = GPIO.PWM(BUZZER, doremi[2])
        elif swstatus == 10:
            p = GPIO.PWM(BUZZER, doremi[3])
        elif swstatus == 1:
            p = GPIO.PWM(BUZZER, doremi[4])
        elif swstatus == 1100:
            p = GPIO.PWM(BUZZER, doremi[5])
        elif swstatus == 1010:
            p = GPIO.PWM(BUZZER, doremi[6])
        elif swstatus == 1001:
            p = GPIO.PWM(BUZZER, doremi[7])
        elif swstatus == 110:
            p = GPIO.PWM(BUZZER, doremi[8])
        else:
            p = None

        if p:
            p.start(75)
            time.sleep(0.3)
            p.stop()
            p = None

except KeyboardInterrupt:
    pass

GPIO.cleanup()
