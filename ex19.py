def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses! " % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for the party!"
	print "Get a blanket.\n"
    
def how_many_cheese_and_crackers_have_remained(cheese_count,boxes_of_crackers):
    print "How many cheese and crackers have remained after the party?"
    print "%d cheeses and %d boxes of crackers." % ((amount_of_cheese - 3),(amount_of_crackers - 5))
     
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do the math inside too:"
cheese_and_crackers(10 + 20 , 5 + 6)	

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "And now for the number of cheese and boxes of crackers that have remained after the party.\n"
amount_of_cheese = 20
amount_of_crackers = 50

how_many_cheese_and_crackers_have_remained(amount_of_cheese,amount_of_crackers)