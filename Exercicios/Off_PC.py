import time
import os
import sys
import turtle


def safe_input(input_message):
    if not sys.stdin:
        sc = turtle.Screen()
        sc.setup(0, 0)
        return turtle.textinput("Sleep Timer", input_message)
    return input(str())


x_time = int(safe_input("Quantos minutos para desligar?"))

time.sleep((x_time * 60))
os.system("shutdown -s")
