from myro import *

def bp(duration, note):
    frequency = 0.0

    if note == 'C':
        frequency = 523.25
    elif note == 'D':
        frequency = 587.33
    elif note == 'E':
        frequency = 659.25
    elif note == 'F':
        frequency = 698.46
    elif note == 'G':
        frequency = 783.99
    elif note == 'A':
        frequency = 880.00
    elif note == 'B':
        frequency = 987.77 
    beep(duration,frequency)

if __name__ == "__main__":
    initialize("/dev/tty.IPRE6-193907-DevB")
    bp(5,'A')
