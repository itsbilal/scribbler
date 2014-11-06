
from myro import *
initialize("/dev/tty.IPRE6-193907-DevB")

DEFAULT_SPEED = -0.1

def goStraight():
	motors(DEFAULT_SPEED, DEFAULT_SPEED)

def turnRightNotch(counter=1):
	for i in range(0,counter):
		turnLeft(0.25, 0.2)

def turnLeftNotch(counter=1):
	for i in range(0, counter):
		turnRight(0.25, 0.2)

"""counter = 0
didGoOffCourse = False"""

while 1:
	right, left = getLine()
	print "left = %d, right = %d" % (left, right)

	if left == 1 and right == 0:
		# Left half is over line
		turnLeftNotch()
		#counter += 1
	elif right == 1 and left == 0:
		# Right half is over line
		turnRightNotch()
		#counter -= 1

	"""elif left == 1 and right == 1:
		if didGoOffCourse:
			if counter >= 1:
				turnRightNotch(counter)
			elif counter <= 1:
				turnLeftNotch(counter)
			didGoOffCourse = False

		counter = 0
	else:
		didGoOffCourse = True"""


	goStraight()
