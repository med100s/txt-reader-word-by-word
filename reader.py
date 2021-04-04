from time import sleep
import os
import pyautogui
import keyboard


def breackifspacepressed():
	if keyboard.is_pressed('space'):  # if key 'q' is pressed 
			print('You Pressed space Key!')
			#if space == False:
			space = True
			while space == True:
					sleep(0.1)
					if keyboard.is_pressed('space'):
						space == False	
						break	



f = open('voina-i-mir.txt', 'r', encoding='utf-8')


f = str(list(f))
b = r"!@#$n,'\—«–»:.-(;)"
for char in b:
    f = f.replace(char," ")
f = f.split(' ')
f = [x for x in f if x]

#print(f)

a = 0
stop = 1961
for i in f:
	if a == 100000:
		break
	if a < stop:              
		print(a, i)
		a += 1
	else:
		
		print(a, i)
		a += 1
		sleep(0.01)

		breackifspacepressed()
			  
		os.system('cls||clear')


