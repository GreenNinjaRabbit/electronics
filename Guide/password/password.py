import signal
from gpiozero import LED, Button

redled = LED(pin=17)
small_button = Button(pin=18, hold_time=2)

redled.blink(on_time=3, off_time=2, n=3, background=False)

def ledon():
    redled.on()
    print("on")

def ledoff():
    redled.off()
    print("off")    

small_button.when_held = ledon
small_button.when_deactivated = ledoff

signal.pause()