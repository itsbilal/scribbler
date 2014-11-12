from myro import *
from line_following import *
from time import sleep
from dominantColor import getColor

from PIL import Image
from tesserwrap import Tesseract

from playnote import bp


initialize("/dev/tty.IPRE6-193907-DevB")

RUN_OVER_TIME = 2
OBSTACLE_THRESHOLD = 600

def getPILImage():
	pic = takePicture("grey")
	savePicture(pic, "current.png")

	img = Image.open("current.png")
	return img

def sanitizeInput(inputStr):
	valid_notes = ["A", "B", "C", "D", "E", "F", "G"]

	inputStr = inputStr.upper()

	for note in valid_notes:
		if note in inputStr:
			return note


goStraight()

while 1:
	correctYourself()
	left, middle,  right = getObstacle()
	if middle >= OBSTACLE_THRESHOLD:
		stop()
		image = getPILImage()
		ocr = Tesseract().ocr_image(image)

		bp(1, sanitizeInput(ocr))

		sleep(1)

	