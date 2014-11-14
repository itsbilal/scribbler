
from myro import *

DEFAULT_SPEED = -0.1

def goStraight():
	motors(DEFAULT_SPEED, DEFAULT_SPEED)

def turnRightNotch(counter=1):
	for i in range(0,counter):
		turnLeft(0.1, 0.2)

def turnLeftNotch(counter=1):
	for i in range(0, counter):
		turnRight(0.1, 0.2)

def correctYourself(lastStep=0):
	right, left = getLine()
	print "left = %d, right = %d" % (left, right)

	if left == 1 and right == 0:
		# Left half is over line
		turnLeftNotch()

		return correctYourself(1)
	elif right == 1 and left == 0:
		# Right half is over line
		turnRightNotch()
		
		return correctYourself(-1)
	elif right == 1 and left == 1:
		goStraight()
		return True
	else:
		if lastStep == -1: # Right
			turnRightNotch()
			return correctYourself(lastStep)
		elif lastStep == 1:
			turnLeftNotch()
			return correctYourself(lastStep)
		else:
			goStraight()
			return False

if __name__ == "__main__":
	initialize("/dev/tty.IPRE6-193907-DevB")
	goStraight()
	while 1:
		correctYourself()




