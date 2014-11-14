from myro import *
from line_following import *
from time import sleep
from dominantColor import getColor

from PIL import Image
from tesserwrap import Tesseract
from playnote import bp
from time import time
from makeSong import makeFile


initialize("/dev/tty.IPRE6-193907-DevB")

RUN_OVER_TIME = 2
OBSTACLE_THRESHOLD = 600

def getPILImage():
	pic = takePicture("grey")
	savePicture(pic, "current.png")

	img = Image.open("current.png")
	return img

def sanitizeInput(inputStr):
	valid_notes = ["A", "B", "C", "D", "E", "F", "G", "Z"]

	inputStr = inputStr.upper()

	for note in valid_notes:
		if note in inputStr:
			return note

def playNotes(notes):
	startTime = 0

	for k in sorted(notes):
		bp(int(int(k - startTime)/4), notes[k])
		startTime = k

	sleep(4)


goStraight()

firstTime = time()

notes = {}

while 1:
	correctYourself()
	left, middle,  right = getObstacle()
	if middle >= OBSTACLE_THRESHOLD:
		stop()
		image = getPILImage()
		ocr = Tesseract().ocr_image(image)
		ocr = sanitizeInput(ocr)

		print "note: %s" % ocr

		if ocr is not None and ocr is not "Z":
			notes[int(time() - firstTime)] = ocr

		elif ocr == "Z":
			playNotes(notes)
			makeFile(notes)
			break

		sleep(1)
		#goStraight()
	
