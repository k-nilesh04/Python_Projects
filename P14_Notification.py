import os 
from plyer import notification
import time

if __name__ == '__main__':
   print("Welcome to Robo Speaker 1.1 Created by Harry")

while True:
  time.sleep(10)
  notification.notify(
    title = "Please Drink Water Now!!", message="Water is good for health", timeout=3)

