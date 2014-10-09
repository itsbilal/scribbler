from myro import *


def turnRightNotch():
	turnRight(0.25,0.2)

def turnLeftNotch():
	turnLeft(0.25,0.25)

def orient():

	max = getObstacle()[1]
	while 1:
		turnRightNotch()
		curObs = getObstacle()[1]
		if curObs < max:
			break
		else:
			max = curObs

	max = 0

	while 1:
		turnLeftNotch()
		curObs = getObstacle()[1]
		if curObs < max:
			break
		else:
			max = curObs

	turnRightNotch()

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



if __name__=="__main__":
	initialize("/dev/tty.IPRE6-193907-DevB")
	setIRPower(130)
	orient()