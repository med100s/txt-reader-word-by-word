from time import sleep
import os
import pyautogui
import keyboard





f = open('6158845.txt', 'r', encoding='utf-8')


f = str(list(f))
b = r"!@#$n,'\—«–»:.-(;)"
for char in b:
    f = f.replace(char," ")
f = f.split(' ')
f = [x for x in f if x]

#print(f)

a = 0
stop = 0
for i in f:
	if a == 100000:
		break
	if a < stop:              
		print(a, i)
		a += 1
	else:
		
		print(a, i)
		a += 1
		#sleep(0.01)

		if keyboard.is_pressed('p') and keyboard.is_pressed('space'):  # if key 'q' is pressed 
			print('You Pressed Pause Key!')
			#if space == False:
			is_space = True
			while is_space == True:
					sleep(0.1)
					if keyboard.is_pressed('p') and keyboard.is_pressed('space'):
						is_space == False	
						break	
			  
		os.system('cls||clear')
