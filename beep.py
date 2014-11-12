from myro import *

def bp(duration, note):
    frequency = 0.0

    if note == 'C':
        frequency = 261.63
    elif note == 'D':
        frequency = 293.66
    elif note == 'E':
        frequency = 329.63
    elif note == 'F':
        frequency = 349.23
    elif note == 'G':
        frequency = 392.00
    elif note == 'A':
        frequency = 440.00
    elif note == 'B':
        frequency = 493.88
    beep(duration,frequency)

if __name__ == "__main__":
    initialize("/dev/tty.IPRE6-193907-DevB")
    bp(5,'A')

