import RPi.GPIO as GPIO
import time

class LEDBar:
  def __init__(self, hours):
    self.hours = hours
    self.pins = []
    self.active_pins = []
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

  def determine_leds(hours):
    pass

  def turn_on_led(pin):
    GPIO.output(pin, True)

  def turn_off_led(pin):
    GPIO.output(pin, False)
