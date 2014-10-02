from myro import *
initialize("/dev/tty.IPRE6-193907-DevB")

from time import sleep

DEFAULT_SPEED = 0.3
MIDDLE_OBSTACLE_THRESHOLD = 1000

setIRPower(130)

sleep(5)

def goStraight():
	motors(DEFAULT_SPEED, DEFAULT_SPEED)

def turnRight90():
	turnRight(1, .75)

def turnLeft90():
	turnLeft(1, .80)

def sweetTurnLeft90():
	move(.6, .5)
	sleep(1.55)
	motors(0, 0)

def turnRightNotch():
	turnRight(1, .1)

def seenObstacle(newThreshold=MIDDLE_OBSTACLE_THRESHOLD):
	left, middle, right = getObstacle()

	print "left: %d, middle: %d, right: %d" % (left, middle, right)

	if middle >= MIDDLE_OBSTACLE_THRESHOLD:
		return True
	else:
		return False

avoidingObstacle = -1

counterForZero = 0
# -1: No obstacle yet
# 0: Obstacle seen, right after first turn to the right
# 1: Walking forward along the box
# 2: Last step

goStraight()

while 1:

	if seenObstacle():
		avoidingObstacle = 0
		turnRight90()
		goStraight()

	if avoidingObstacle >= 0 and avoidingObstacle <= 1:
		sleep(2)

		# Check the side
		turnLeft90()
		if seenObstacle(300):
			turnRight90()
		else:
			turnRight90()
			sweetTurnLeft90()
			avoidingObstacle += 1

		if avoidingObstacle == 0:
			counterForZero += 1

		goStraight()
	elif avoidingObstacle == 2:
		# Go forward for counter * 2 seconds
		sleep(2*counterForZero)
		avoidingObstacle = -1
		turnRight90()
		goStraight()

	print "avoidingObstacle: %d" % avoidingObstacle


