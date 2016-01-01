def add(a,b):
	print "Adding %d and %d " % (a,b)
	return a + b

def subtract(a,b):
	print "Subtracting %d + %d " % (a,b)
	return a - b

def divide(a,b):
	print "Dividing %d / %d " % (a,b)
	return a / b

def multiply(a,b):
	print "Multiplying %d * %d " % (a,b)
	return a * b

print "Let's do some math with just functions!"

Age = add(30,5)
Height = subtract(78,4)
Weight = multiply(90,2)
iQ = divide(100,2)


print "Age: %d, Height: %d, Weight: %d, iQ: %d  \n" %(Age,Height,Weight,iQ)

#A puzzle for the extra credit, type it anyway
print "Here is a puzzle."

what = add(Age, subtract(Height,multiply(Weight,divide(iQ, 2))))

print "That becomes: ", what, "Can you do it by hand?"






