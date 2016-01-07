the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies',2,'dimes',3,'quarters']

#loop goes through list
for number in the_count:
    print "A fruit of type: %d " % number

#loop goes through list
for fruit in fruits:
    print "This is count %s " % fruit

#loop goes through mixed list
for i in change:
    print "I got %r " % i

#building lists
elements = []

#using range function to count from 0 to 5 counts
for i in range(0,6):
    print "Adding %d to the list." % i
    #append function
    elements.append(i)
    
#print elements
for i in elements:
    print "Element was: %d " % i                 