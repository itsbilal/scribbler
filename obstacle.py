from myro import *
initialize("/dev/tty.IPRE6-193907-DevB")

bump = 1000.0
space = 400.0
def main():
	motors(0.5,0.5)
	while 1:
		L,C,R=getObstacle()
		print 'Left: {} Centre: {} Right: {}'.format(L, C, R)
                if C > bump:
                    motors(0.5,-0.5)
                elif L < space:
                    motors(0.3,0.5)
                else:
                    motors(0.5,0.5)

main()
