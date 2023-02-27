# Author: Seamus Flannery
# Run this file from the command line, all functions are called in the executable.
i = 0
s = 0

nmax = int(input("How high does your harmonic tower go?"))
while i < nmax:
    i += 1
    s += 1/i

print("Harmonic sum up to " + str(nmax) + " is ", s)
