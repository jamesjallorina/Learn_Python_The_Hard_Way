#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from : {from_file} to : {to_file}. ")
print("Ready, hit RETURN to continu, CTRL-C to abort.")
input()

infile = open(from_file)

outfile = open(to_file, 'w')

outfile.write(infile.read())

print("Done!")

infile.close()
outfile.close()
