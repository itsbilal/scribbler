from myro import *

def getColor(): 
	picture = takePicture("color")
	show(picture)
	blue = 0
	green = 0
	red = 0

	for pixel in getPixels(picture):
		r,g,b = getRGB(pixel)
		red += r
		green += g
		blue += b


	print "red = %d, green = %d, blue = %d" % (red, green, blue)

	if red > green and red > blue:
		print "Dominant colour: red"
	elif green > red and green > blue:
		print "Dominant colour: green"
	else:
		print "Dominant colour: blue"


if __name__ == "__main__":
	initialize("/dev/tty.IPRE6-193907-DevB")
	getColor()

