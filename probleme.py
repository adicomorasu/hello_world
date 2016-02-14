#!/usr/local/bin/python
# import ipdb
from sys import argv, exit

if len(argv) != 3:
    print "Not enough arguments!"
    exit()

filename = argv[1]
numlines = int(argv[2])

print "We're going to edit %r." % filename
print "Opening the file..."
target = open(filename, 'w')

# numlines = int(raw_input("Now I'm going to ask you for how many lines: "))
lines = []

for i in range(1, numlines + 1):
    line = raw_input("line %d: " % i)
    lines.append(line)

print "I'm going to write these to the file."


for i in lines:
    target.write(i)
    target.write('\n')

print "And finally, we close it."
target.close()
