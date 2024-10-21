import RPi.GPIO as GPIO
import time

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24
SW = [0, 5, 6, 13, 19]
SWstatus = [0, 0, 0, 0, 0]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
for i in range(1,5):
    GPIO.setup(SW[i],GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

L_Motor = GPIO.PWM(PWMA,500)
R_Motor = GPIO.PWM(PWMB,500)
L_Motor.start(0)
R_Motor.start(0)
Motor_Control = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0]
try:
    while True:
        for i in range(1,5):
            if GPIO.input(SW[i]) == 1:
                GPIO.output(AIN1,Motor_Control[4*i])
                GPIO.output(AIN2,Motor_Control[4*i+1])
                GPIO.output(BIN1,Motor_Control[4*i+2])
                GPIO.output(BIN2,Motor_Control[4*i+3])
                L_Motor.ChangeDutyCycle(100)
                R_Motor.ChangeDutyCycle(100)
                time.sleep(0.05)

                GPIO.output(AIN1,Motor_Control[4*i])
                GPIO.output(AIN2,Motor_Control[4*i+1])
                GPIO.output(BIN1,Motor_Control[4*i+2])
                GPIO.output(BIN2,Motor_Control[4*i+3])
                L_Motor.ChangeDutyCycle(0)
                R_Motor.ChangeDutyCycle(0)


        

except KeyboardInterrupt:
    pass

GPIO.cleanup()
