import time
import pyautogui
from os import getenv
from dotenv import load_dotenv

load_dotenv()
pyautogui.PAUSE = .1
pyautogui.FAILSAFE = True
TYPING_SPEED = .005
time.sleep(2)

# This function will press a key given number of times
def pressKey(keyToPress, numOfPresses = 1):
    for _ in range(numOfPresses):
        pyautogui.press(keyToPress)

# First name
pressKey("tab")
pyautogui.write('Glenn', interval = TYPING_SPEED)

# Last name
pressKey("tab")
pyautogui.write('Antony Sheen', interval = TYPING_SPEED)

# E-mail
pressKey("tab")
pyautogui.write(getenv('EMAIL_ID'), interval = TYPING_SPEED)

# How long would you like to work for Pret?
pressKey("tab")
pressKey("space")

# What days are you available to work?
pressKey("tab", 10)
pressKey("space")

# On the days you have selected, please let us know the earliest time you can start work
pressKey("tab")
pressKey("space")

# On the days you have selected, please let us know the latest time you can finish work on a day shift
pressKey("tab")
pressKey("right", 14)

# 35 hours is full time and the minimum part time hours are 16. Choose the option that suits you best
pressKey("tab", 3)
pressKey("space")

# Are you over 18?
pressKey("tab")
pressKey("space")

# Do you have any unspent criminal convictions under the rehabilitation of offenders act 1974?
pressKey("tab")
pressKey("right")

# Tell us why you would like to join the Pret family?
pressKey("tab")
pyautogui.write('I would like to join the Pret family because I am passionate about providing delicious food and excellent customer service. I appreciate Pret\'s commitment to using fresh, high-quality ingredients and their dedication to sustainability. I believe my skills and enthusiasm would be a great fit for the Pret team, and I am excited about the opportunity to contribute to a company that values both its customers and its employees.', interval = TYPING_SPEED)

# Have you worked at Pret before?
pressKey("tab")
pressKey("right")

# Address
pressKey("tab")
pyautogui.write('100 Cavendish Dr\nLondon E11 1DL', interval = TYPING_SPEED)

# City
pressKey("tab")
pyautogui.write('London', interval = TYPING_SPEED)

# Postcode
pressKey("tab")
pyautogui.write('E11 1DL', interval = TYPING_SPEED)

# Phone number
pressKey("tab")
pyautogui.write('07760782072', interval = TYPING_SPEED)

# Have you worked at Pret before?
pressKey("tab")
pressKey("right")

pressKey("tab", 3)