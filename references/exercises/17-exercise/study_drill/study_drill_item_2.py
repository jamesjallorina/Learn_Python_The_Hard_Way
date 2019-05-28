#!/usr/bin/python

from sys import argv
#from os.path import exists
import shutil

script, from_file, to_file = argv
shutil.copyfile(from_file, to_file)
