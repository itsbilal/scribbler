from myro import *
from time import sleep

def turnRightNotch(notches=1):
	for i in range(0, notches):
		turnRight(0.25,0.2)

def turnLeftNotch():
	turnLeft(0.25,0.25)

def orient():
	totalNotches = 0
	max = getObstacle()[1]
	while 1:
		turnRightNotch()
		totalNotches += 1
		curObs = getObstacle()[1]
		if curObs < max and curObs == 0:
			break
		else:
			max = curObs

	max = 0
	noMax = 0

	while 1:
		turnLeftNotch()
		totalNotches -= 1
		curObs = getObstacle()[1]
		if curObs < max and noMax == 1:
			break
		elif curObs < max and noMax == 0:
			noMax += 1
			max = curObs
		else:
			max = curObs
			noMax = 0

	turnRightNotch(2)

	"""for i in range(CIRCLECOUNTS):
		L,C,R = getObstacle()
		obstaclevalues += [C]
		turnRightNotch()

	max = 0
	index =0

	for i in range(len(obstaclevalues)):
		if obstaclevalues[i] > max:
			max = obstaclevalues[i]
			index = i 


	print "max=%d, index=%d" % (max, index)

	turnRight(1,0.1*index)"""

	return totalNotches



if __name__=="__main__":
	initialize("/dev/tty.IPRE6-193907-DevB")
	setIRPower(130)
	orient()