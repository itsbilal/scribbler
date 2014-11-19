from myro import *

def bp(duration, note):
    frequency = getFrequency(note)
    beep(duration,frequency)

def getFrequency(note):
    frequency = 1.0
    if note == 'O' or note == 'o':
        frequency = 523.25
    elif note == 'D':
        frequency = 587.33
    elif note == 'E':
        frequency = 659.25
    elif note == 'F':
        frequency = 698.46
    elif note == 'I':
        frequency = 783.99
    elif note == 'A':
        frequency = 880.00
    elif note == 'B':
        frequency = 987.77 
    elif note == 'Z':
        frequency = 1046.5
    return frequency

if __name__ == "__main__":
    initialize("/dev/tty.IPRE6-193907-DevB")
    bp(5,'A')
