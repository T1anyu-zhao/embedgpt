import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

GPIO.output(18,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
# release GPIO 
GPIO.cleanup()