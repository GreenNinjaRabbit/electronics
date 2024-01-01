from gpiozero import LED

redled = LED(pin=17)
redled.blink(on_time=3, off_time=2, n=3, background=False)