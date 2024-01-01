#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/26
########################################################################
from gpiozero import LED
from time import sleep

print ('Program is starting ... ')

led = LED(17)           # define LED pin according to BCM Numbering
# led = LED("J8:11")     # BOARD Numbering
'''
# pins numbering, the following lines are all equivalent
led = LED("GPIO17")     # BCM
led = LED("BCM17")      # BCM
led = LED("BOARD11")    # BOARD
led = LED("WPI0")       # WiringPi
led = LED("J8:11")      # BOARD
'''

def flash(what, wait):
    what.on()
    sleep(wait)
    what.off()
    sleep(wait)

def dot():
    flash(led, 0.2)

def dash():
    flash(led, 0.5)

def newword():
    sleep(2.5)

morsecode = {
    "E": [dot],
    "L": [dot,dash,dot,dot],
    "O": [dash,dash,dash],
    "S": [dot,dot,dot],
    " ": [newword]
}

def morse(letter):
    letter = letter.upper()
    for d in morsecode[letter]:
        d()
    print(f"{letter}", end="", flush=True)
    if d == dot:
        sleep(0.8)
    else:
        sleep(0.5)

def decode(words):
    for letter in words:
        morse(letter)

while True:
    decode("leo SOS ")