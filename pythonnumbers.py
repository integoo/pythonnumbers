import random
import os

contador=0
correctas=0
efectividad=0
while 1==1:
	contador=contador + 1
	x = random.randint(10,99)
	y = random.randint(10,99)
	print(str(x) +" + " + str(y) + " = ")
	result = input()
	if x+y == int(result):
		# print("BIEN")
		correctas = correctas + 1
		clear = lambda: os.system('clear')
		clear()
	else:
		print("MAL")
		os.system('say "The result is wrong"')
		os.system('afplay /System/Library/Sounds/Sosumi.aiff')
	efectividad = correctas / contador * 100
	print("Efectividad " + str(int(efectividad)) + "%")
