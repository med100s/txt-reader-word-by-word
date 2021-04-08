from time import sleep
import os
import pyautogui
import keyboard

f = open('filip_kotler-osnovi_marketinga-1499658489.txt', 'r', encoding='utf-8')


f = str(list(f))
b = r"!@#$n,'\—«–»:.-(;)"
for char in b:
    f = f.replace(char," ")
f = f.split(' ')
f = [x for x in f if x]

#print(f)

def make_pause(is_pause = False):
	while True:
		if keyboard.is_pressed('space'):
			is_pause = True

		while is_pause == True:
			print('pause started')
			sleep(3)
			if keyboard.is_pressed('space'):
				print('pause stoped')
				break
		break

def show_data(f):
	is_pause = False
	word_id = 0	
	stop = 1000
	for i in f:
		if word_id == 100000:
			break
		if word_id < stop:              
			print(word_id, i)
			word_id += 1
		else:
			
			print(word_id, i)
			word_id += 1
			sleep(1)

			make_pause()



			os.system('cls||clear')

show_data(f)
