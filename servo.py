servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(angle):
    deg = ( 0.5 + (1.9 / 180) * angle )*5
    servo.ChangeDutyCycle(deg)
    time.sleep(1.0)



for i in range(3):
    servo.ChangeDutyCycle(2.5)
    time.sleep(1)
    setservo(75)

GPIO.cleanup()