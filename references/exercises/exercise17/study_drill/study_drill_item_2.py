#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

data = open(from_file).read()
file = open(to_file, 'w').write(data)

