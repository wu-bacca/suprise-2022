import soundboard
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

sb = soundboard.SoundBoard() # Playsound when button is pressed

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        sb.play_sound()
        print("Button was pushed!")
        time.sleep(3)
