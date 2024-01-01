from gpiozero import LED, Button

redled = LED(pin=17)
small_button = Button(pin=18)

redled.blink(on_time=3, off_time=2, n=3, background=False)

while True:
    if small_button.is_held:
        redled.on()
    else:
        redled.off()