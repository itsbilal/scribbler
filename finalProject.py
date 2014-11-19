from myro import *
from line_following import *
from time import sleep
from dominantColor import getColor

from PIL import Image
from tesserwrap import Tesseract
from playnote import bp
from time import time, strftime
from makeSong import makeFile

import math

initialize("/dev/tty.IPRE6-193907-DevB")

RUN_OVER_TIME = 2
OBSTACLE_THRESHOLD = 600

INTERVAL_BETWEEN_TURNS= 4

def getPILImage(should_save=True):
	pic = takePicture("grey")
	savePicture(pic, "current.png")

	if should_save:
		savePicture(pic, "photos/"+strftime("%Y-%m-%d %H:%M:%S")+".png")

	img = Image.open("current.png")
	return img

def sanitizeInput(inputStr):
	valid_notes = ["A", "B", "C", "G", "Z"]

	inputStr = inputStr.upper()

	for note in valid_notes:
		if note in inputStr:
			return note

def playNotes(notes):
	startTime = 0

	for k in sorted(notes):
		bp(int(int(k - startTime)/16), notes[k])
		startTime = k

	sleep(4)

def turnRight90():
	turnRight(.5, 1.33)

def turnLeft90():
	turnLeft(.5, 1.32)

goStraight()

firstTime = time()
lastTurnTime = time()

notes = {}

while 1:
	correctionTime = time()
	if not correctYourself():
		stop()
		playNotes(notes)
		makeFile(notes, firstTime, filename=("sounds/" + strftime("%Y-%m-%d %H:%M:%S")+".wav"))
		break
	correctionTime = time() - correctionTime

	lastTurnTime = lastTurnTime + math.floor(correctionTime) # Move the last turn time forward
	curTime = time()

	print "correctionTime = %d, lastTurnTime = %d, curTime=%d" % (correctionTime, lastTurnTime, curTime)

	if (curTime - lastTurnTime) > INTERVAL_BETWEEN_TURNS:
		stop()
		turnLeft90()

		image = getPILImage()
		ocr = Tesseract().ocr_image(image)
		ocr = sanitizeInput(ocr)

		if ocr is None:
			image = getPILImage(False)
			ocr = Tesseract().ocr_image(image)
			ocr = sanitizeInput(ocr)

			if ocr is None:
				image = getPILImage(False)
				ocr = Tesseract().ocr_image(image)
				ocr = sanitizeInput(ocr)

		print "note: %s" % ocr

		if ocr is not None:
			notes[int(time() - firstTime)] = ocr

		turnRight90()
		lastTurnTime = time()
		goStraight()

