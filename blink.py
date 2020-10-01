#python code to blink an LED using a Rasp Berry Pi 3 model B version 1.2
#Materials needed are a breadboad, 100ohm resistor, red LED, 5V power supply, keyboard and mouse

#We use PIN 11 or GPIO 17 in this case



import RPi.GPIO as GPIO #import rasp berry pi GPIO

from time import sleep #import sleep function from the time module

GPIO.setmode(GPIO.BOARD) #we want to use physical pin numbering

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) #set pin 11 as an output and initializing it to low(off)

while True: #Forever loop

    GPIO.output(11, GPIO.HIGH) #Turn on the LED

    sleep(0.1) #Wait for one tenth second
    
    GPIO.output(11, GPIO.LOW) #Turn off the LED

    sleep(0.1) #wait for one tenth second
