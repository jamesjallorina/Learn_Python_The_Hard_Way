#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

file = open(from_file)
data = file.read()
file.close()
file = open(to_file, 'w')
file.write(data)
file.close()
