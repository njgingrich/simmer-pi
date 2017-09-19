import RPi.GPIO as GPIO
import time

class LEDBar:
  def __init__(self):
    self.minutes = 0
    self.leds = {1: 14, 2: 15, 3: 18, 4: 23, 5: 24, 6: 25, 7: 8, 8: 7}
    self.active_leds = []
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for key, val in self.leds.items():
      GPIO.setup(val, GPIO.OUT)
    self.determine_leds(self.minutes)

  def determine_leds(self, minutes):
	self.turn_on_led(1)
	time.sleep(2)
	self.turn_off_led(1)

  def turn_on_led(self, LED):
    GPIO.output(self.leds[LED], GPIO.HIGH)

  def turn_off_led(s6elf, LED):
    GPIO.output(self.leds[LED], GPIO.LOW)


def test():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  for key, val in leds.items():
    print(key, val)
    GPIO.setup(val, GPIO.OUT)

  print('LED on')
  for key, val in leds.items():
    GPIO.output(val, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(val, GPIO.LOW)
  for key, val in leds.items():
    GPIO.output(val, GPIO.HIGH)
  time.sleep(2)
  print('LED off')
  for key, val in leds.items():
    GPIO.output(val, GPIO.LOW)
