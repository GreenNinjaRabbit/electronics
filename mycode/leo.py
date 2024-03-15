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

def dot():
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)

def dash():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

def l():
    dot()
    dash()
    dot()
    dot()
    print("L", end="", flush=True)
    sleep(0.8)

def e():
    dot()
    print("E", end="", flush=True)
    sleep(0.8)

def o():
    dash()
    dash()
    dash()
    print("O", end="", flush=True)
    sleep(0.5)

def newword():
    print("")
    sleep(3)

while True:
    l()
    e()
    o()
    newword()