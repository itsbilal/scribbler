from myro import *
from line_following import *
from time import sleep
from dominantColor import getColor

from PIL import Image
from tesserwrap import Tesseract
from playnote import bp
from time import time, strftime
from makeSong import makeFile

initialize("/dev/tty.IPRE6-193907-DevB")

RUN_OVER_TIME = 2
OBSTACLE_THRESHOLD = 600

INTERVAL_BETWEEN_TURNS= 4

def getPILImage():
	pic = takePicture("grey")
	savePicture(pic, "current.png")
	savePicture(pic, "photos/"+strftime("%Y-%m-%d %H:%M:%S")+".png")

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

def turnRight90():
	turnRight(.5, 1.30)

def turnLeft90():
	turnLeft(.5, 1.32)

goStraight()

firstTime = time()
lastTurnTime = time()

notes = {}

while 1:
	if not correctYourself():
		stop()
		playNotes(notes)
		makeFile(notes, firstTime, filename=("sounds/" + strftime("%Y-%m-%d %H:%M:%S")+".wav"))
		break

	curTime = time()

	if (curTime - lastTurnTime) > INTERVAL_BETWEEN_TURNS:
		stop()
		turnLeft90()

		image = getPILImage()
		ocr = Tesseract().ocr_image(image)
		ocr = sanitizeInput(ocr)

		print "note: %s" % ocr

		if ocr is not None and ocr is not "Z":
			notes[int(time() - firstTime)] = ocr

		elif ocr == "Z":
			playNotes(notes)
			makeFile(notes, firstTime, filename=("sounds/" + strftime("%Y-%m-%d %H:%M:%S")+".wav"))
			break

		turnRight90()
		lastTurnTime = curTime
		goStraight()

