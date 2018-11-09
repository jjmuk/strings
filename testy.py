#import time

#localtime = time.asctime(time.localtime(time.time()))
#print "Local current time :", localtime
#name = input("What is your name? ")
# a = [1,1,2,3,5,8,13,21,34,55,89]
# b= [1,2,3,4,5,6,7,8,9,10,11,12,13]
# y = []

a = input("Please enter a word: ")
n = len(a) - 1
c = 0
w = 0
b = []
y = []
anew = []

#b = a
print (b)
for i in a:
	
	    #print (a[n])
	b.append(a[n])
	anew.append(a[w])
	    #if b[c] == a[n]:
	    #b[c] == a[n]
	n -= 1
	c += 1
	w += 1
	if n < 0 :
		break
    
print
print (b)

for item in a:
	if item in b:
		y.append(item)
		#print ("a is a palindrome")
	else:
		print ("a is not a palindrome")
        
	    
print (y)

e = 0
f = 0	    	
for i in y:
	for i in anew:
		if y[e] in anew[f]:
			e += 1
			f += 1
			if e == len(y):
				break
		else:
			print ("a is not a palindrome")
print ("a is a palindrome")






			

		
			




      


		
	