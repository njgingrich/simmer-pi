import RPi.GPIO as GPIO
import time
import atexit

class Bar:
  def __init__(self):
    self.minutes = 0
    self.leds = {1: 14, 2: 15, 3: 18, 4: 23, 5: 24, 6: 25, 7: 8, 8: 7}
    self.active_leds = []
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for key, val in self.leds.items():
      GPIO.setup(val, GPIO.OUT)
      atexit.register(self.turn_off_pin, val)

  def determine_leds(self, minutes):
    self.minutes = minutes
    # turn on LEDs 1 thru (minutes / 180)
    highest = int(self.minutes / 180)
    for led in range(1, highest + 1):
      print('turning on led {0}').format(led)
      self.turn_on_pin(self.leds[led])

  def turn_on_pin(self, pin):
    GPIO.output(pin, GPIO.HIGH)

  def turn_off_pin(self, pin):
    GPIO.output(pin, GPIO.LOW)
