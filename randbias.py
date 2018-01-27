import time
from time import sleep
import math

previous=0
resetprevious=0

def getseed():
	global previous
	sleep(0.000001) #Convergers pretty fast without sleep
	previous = time.time()
	#print(previous)


def customrandmin():
	'''Returns values between [0,1)
	Uses time as seed to generate a random number and needs to sleep to allow time to change because need to handle the case
	when the user calls the function in a loop. Can be handled without using sleep by saving the previous value (in case we need an array of random values).
	'''
	global previous
	global resetprevious
	if resetprevious < 15:
		randtime = ((previous * 9))
		resetprevious+=1
	else:
		resetprevious = 0
		getseed()
		randtime = (((previous + 11) * 9))
			
	
	previous = randtime
	randtime = randtime % 100
	randret = (math.floor(randtime)) / 100
	return randret


def customrandomrange(ll,ul):
	#Returns values including [ll,ul] i.e range using the customrandmin function.
	temp = customrandmin()	
	ans = int(ll + (temp * ((ul - ll) + 1)))
	return ans

getseed()

print("Enter range in format ||X,Y||")
temp = input().split(',')

print("Enter the amount of random numbers you need")
limit = int(input().strip())

lowerlimit = int(temp[0])
upperlimit = int(temp[1])


countfav=0
countunfav=0

for i in range(limit):
	
	temprand = customrandomrange(0,100)
	'''Using the above function we get a random number between 0 and 100. If the number is < 73 we get our random number from
		the upper range(Where we want higher bias otherwise the lower range.)
		'''	
	if temprand < 73:
		print (customrandomrange(math.floor((upperlimit/2))+1,upperlimit),end=' ')
		countfav+=1
	else:
		print (customrandomrange(lowerlimit,math.floor(upperlimit/2)),end=' ') 
		countunfav+=1

print("\nDo you want see the Favourable/UnFavourable Outcomes amount? Y/N")
check = input().upper()

if check == "Y":
	print("Favourable   : ",countfav)
	print("Unfavourable : ",countunfav)
	