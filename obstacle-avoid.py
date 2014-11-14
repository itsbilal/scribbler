from myro import *

if __name__ == "__main__":
	initialize("/dev/tty.IPRE6-193907-DevB")

import orient

from time import sleep

DEFAULT_SPEED = 0.3
MIDDLE_OBSTACLE_THRESHOLD = 100

TIME_BETWEEN_CHECKES=1

ANGULAR_CHECKS=True

if ANGULAR_CHECKS == False:
	MIDDLE_OBSTACLE_THRESHOLD = 700

setIRPower(130)

sleep(5)

def goStraight():
	motors(DEFAULT_SPEED, DEFAULT_SPEED)

def turnRight90():
	turnRight(.5, 1.30)

def turnLeft90():
	turnLeft(.5, 1.32)

def sweetTurnLeft90():
	move(.65, .5)
	sleep(1.6)
	motors(0, 0)

def seenObstacle(newThreshold=MIDDLE_OBSTACLE_THRESHOLD):
	left, middle, right = getObstacle()

	print "left: %d, middle: %d, right: %d" % (left, middle, right)

	if middle >= MIDDLE_OBSTACLE_THRESHOLD:
		return True
	else:
		return False

avoidingObstacle = -1
# -1: No obstacle yet
# 0: Obstacle seen, right after first turn to the right
# 1: Walking forward along the box
# 2: Last step

counterForZero = 1

notches = 0

goStraight()

while 1:

	if seenObstacle():
		if ANGULAR_CHECKS:
			notches = orient.orient()
		else:
			notches = 0
		print "notches = %d" % notches
		avoidingObstacle = 0
		turnRight90()
		goStraight()

	if avoidingObstacle >= 0 and avoidingObstacle <= 1:
		sleep(TIME_BETWEEN_CHECKES)

		# Check the side
		turnLeft90()
		if seenObstacle(300):
			turnRight90()
		else:
			turnRight90()
			sweetTurnLeft90()
			if avoidingObstacle == 0:
				goStraight()
				sleep(1.0)
				if notches <= -2:
					sleep(2)
					orient.turnRightNotch(abs(notches))
					avoidingObstacle = -2
					goStraight()
				else:
					turnLeft90()
					if ANGULAR_CHECKS:
						orient.orient()
					turnRight90()

			avoidingObstacle += 1

		if avoidingObstacle == 0:
			counterForZero += 1

		goStraight()
	elif avoidingObstacle == 2:
		# Go forward for counter * 2 seconds
		print "counterForZero: %d" % counterForZero
		sleep(TIME_BETWEEN_CHECKES*counterForZero)
		avoidingObstacle = -1
		if notches >= 2:
			sleep(2)
			orient.turnRightNotch(abs(notches))
		else:
			turnRight90()
		goStraight()

	print "avoidingObstacle: %d" % avoidingObstacle


