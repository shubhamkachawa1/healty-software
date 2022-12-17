import time as T
import  os
import pygame

m=1
s=0
set={0}

stard_eye=1
stard_workout=2
stard_water=3

stard_eye+=1
stard_workout+=1
stard_water+=1


def show_img(till):
	global size
	flage=1

	pygame.init()
	w = 1300
	h = 1000
	size = (w, h)
	pygame.display.set_caption('image')
	img = pygame.image.load("eye.jpg")
	screen = pygame.display.set_mode(size)
	screen.blit(img, (0, 0))
	#pygame.display.update()
	pygame.display.flip()
	while(till!=0):
		T.sleep(1)
		till=till-1
		print("hai")

	pygame.quit()
	return 0

		

set.remove(list(set)[0])

def delete():
	global set
	set.remove(list(set)[0])
	

def eye():
	print("eye")

	global s
	global m
	global set

	global stard_workout
	global stard_water
	ey=29
	while (1):
		pygame.init()
		w = 1300
		h = 1000
		size = (w, h)
		# 	pygame.display.set_caption('image')
		screen = pygame.display.set_mode(size)
		img = pygame.image.load("eye.jpg")
		img = pygame.transform.scale(img, size).convert_alpha()
		screen.blit(img, (0, 0))
		pygame.display.update()

		if(s>=59):
			m=int(m+s/59)
			s=s%59
		if(ey==0):
			chack()
		if(m%stard_workout==0 and s==0):
			set.add(2)
		if(m%stard_water==0 and s==0):
			set.add(3)
		T.sleep(1)
		s=s+1
		ey=ey-1
	return 0

		
	
def workout():
	global s
	global m
	global set
	
	global stard_eye
	global stard_water
	
	wk=29
	while(1):
		T.sleep(1)
		
		if(s>=59):
			m=m+s//59
			s=s%59
			
		if(wk==0):
			os.system("clear")
			chack()
		if(m%stard_eye==0 and s==0):
			set.add(1)
		if(m%stard_water==0 and s==0):
			set.add(3)
		s=s+1
		wk=wk-1
		print("workout  ",set)
			
	
def water():
	show_img(30)
	global s
	global m
	global set
	
	global stard_eye
	global stard_workout
	
	wa=29
	while(1):
		T.sleep(1)
		
		if(s>=59):
			m=m+s//59
			s=s%59
			
		if(wa==0):
			os.system("clear")
			chack()
		if(m%stard_eye==0 and s==0):
			set.add(1)
		if(m%stard_workout==0 and s==0):
			set.add(2)
		s=s+1
		wa=wa-1
		print("water ",set)

def scipe():
	global s
	global m
	while(1):

		if(s>58):
			m=int(m+s/59)
			s=int(s%59)
			break
		T.sleep(1)
		s += 1
	return 0
	

	

def chack():



	global m
	global set
	global s
	
	global stard_eye
	global stard_workout
	global stard_water
	
	
	while(1):
		if (len(list(set)) != 0):
			if (list(set)[0] == 1):
				delete()
				eye()

			if (list(set)[0] == 2):
				delete()
				workout()

			if (list(set)[0] == 3):
				delete()
				water()
		elif (m % stard_eye == 0 and s==0):
			eye()
		elif(m % stard_workout == 0 and s==0):
			workout()
		elif (m % stard_water == 0 and s==0):
			water()


		scipe()
		print("  ",m)
		print(set)
		
chack()
T.sleep(2)
while(1):
	pygame.init()
	w = 1300
	h = 1000
	size = (w, h)
# 	pygame.display.set_caption('image')
	screen = pygame.display.set_mode(size)
	img = pygame.image.load("eye.jpg")
	img=pygame.transform.scale(img,size).convert_alpha()
	screen.blit(img, (0, 0))
	pygame.display.update()
	#pygame.display.flip()

#while(1):
	#show_img(2)
#eye()