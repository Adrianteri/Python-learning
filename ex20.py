from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
    
#read ....read as bytes and return string from the file

def rewind(f):
    f.seek(0)
    
# Seek ..Move to new file position     

def print_a_line(line_count,f):
	print line_count,f.readline(),
    
#readline... takes in the size as an arg an reads a lne from s file as a string

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)	


