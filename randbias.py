import random
import time
from time import sleep
import math

def customrandmin():
	#Returns values between [0,1)
	randtime = (9999 * time.time() % 100)
	randret = (math.floor(randtime)) / 100
	return randret


def customrandomrange(ll,ul):
	#Returns values including [ll,ul] i.e range
	temp = customrandmin()
	
	ans = int(ll + (temp * ((ul - ll) + 1)))
	return ans

print("Enter range in format ||X,Y||")

temp = input().split(',')

lowerlimit = int(temp[0])
upperlimit = int(temp[1])


for i in range(100):
	sleep(0.0000001)
	temprand = customrandomrange(0,100)	
	# print("randseed : " ,temprand)
	if temprand < 73:
		print (customrandomrange(math.floor((upperlimit/2))+1,upperlimit))
	else:
		print (customrandomrange(lowerlimit,math.floor(upperlimit/2))) 

