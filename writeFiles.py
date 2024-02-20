#!/usr/bin/env python3
from os import strerror

#version 1

try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


try:
	for line in open('newtext.txt', 'rt'):
		print(line)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

#version 2

try:
    file = open('newtext.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

try:
	for line in open('newtext.txt', 'rt'):
		print(line)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
