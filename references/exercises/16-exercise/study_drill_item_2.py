#!/usr/bin/pyhon

from sys import argv

script, filename = argv

print(f"We're going to read the file: {filename} with script: {script}. ")

filehandler = open(filename)

print(filehandler.read())

print(f"closing the file: {filename}.")
