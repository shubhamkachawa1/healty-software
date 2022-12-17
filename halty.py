import time as t
import  pygame

start_eye=30
start_workout=50
start_water=45



menetus=0
second=0

starting_menetus=t.time()/59
starting_second=t.time()

def enisilize_menetus_second():
	global starting_menetus
	global starting_second
	
	global menetus
	global second
	
	now_menetus=t.time()/59
	now_second=t.time()
	
	second=int((now_second+1)-starting_second)
	menetus=int((now_menetus+1)-starting_menetus)

	return  0
	
def eye():
        ey = 59*1
        pygame.init()
        w = 1300
        h = 1000
        size = (w, h)
        screen = pygame.display.set_mode(size)
        while (1):
                img = pygame.image.load("eye.jpg")
                screen.blit(img, (0, 0))
                pygame.display.update()
                if(ey==0):
                        pygame.quit()
                        chack()
                t.sleep(1)
                ey=ey-1
        return 0

def workout():
	ey = 59*1.5
	pygame.init()
	w = 1300
	h = 1000
	size = (w, h)
	screen = pygame.display.set_mode(size)
	while (1):

		img = pygame.image.load("workout.jpg")
		screen.blit(img, (0, 0))
		pygame.display.update()
		if(ey==0):
			pygame.quit()
			chack()
		t.sleep(1)
		ey=ey-1
	return 0

def water():
	ey = 59*1
	pygame.init()
	w = 1300
	h = 1000
	size = (w, h)
	screen = pygame.display.set_mode(size)
	while (1):
		img = pygame.image.load("water.jpg")
		screen.blit(img, (0, 0))
		pygame.display.update()
		if(ey==0):
			pygame.quit()
			chack()
		t.sleep(1)
		ey=ey-1
	return 0

	
def chack():
	global second
	global menetus
	
	global start_eye
	global start_workout
	global start_water
	while(1):
		
		enisilize_menetus_second()
		if ( menetus % start_eye  == 0 and second%59==0):
			eye()
		elif(menetus % start_workout == 0 and second%59==0):
			workout()
		elif(menetus % start_water ==0 and second%59==0):
			water()
	return  0	

chack()
