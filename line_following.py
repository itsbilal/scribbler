
from myro import *
initialize("/dev/tty.IPRE6-193907-DevB")

DEFAULT_SPEED = 0.1

def goStraight():
	motors(DEFAULT_SPEED, DEFAULT_SPEED)

def turnRightNotch():
	turnRight(0.25, 0.2)

def turnLeftNotch():
	turnLeft(0.25, 0.2)

while 1:
	right, left = getLine()
	print "left = %d, right = %d" % (left, right)

	if left == 1 and right == 0:
		turnLeftNotch()
	elif right == 1 and left == 0:
		turnRightNotch()

	goStraight()
