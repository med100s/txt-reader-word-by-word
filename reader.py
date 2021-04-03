from time import sleep
import os

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
		os.system('cls||clear')

		
