# import the argument variable module (for command line args)

from sys import argv

#define how many args that the script will accept

script , filename = argv

#create a var that will hold the opened file
txt = open(filename)

#prompt for the filename and open and read from it
print " Here's your file %r:" % filename
print txt.read()

#create another var that will hold the filename 'again'
print "Type the filename again:"
file_again = raw_input()

#var that holds the opened file 'again'
txt_again = open(file_again)

#open the file and read from it 'again'
print txt_again.read()
        
