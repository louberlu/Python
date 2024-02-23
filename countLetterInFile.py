#!/usr/bin/env python3
from os import strerror
import string as s

alphaCount = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
'h': 0,'i': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 
'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

filename = input("Enter the file's name: ")
try:
    file = open(filename, 'rt')
    content = file.read()
    for char in content:
        if char.isalpha():
            alphaCount[char.lower()]+=1
    file.close()
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

for key in alphaCount.keys():
    if alphaCount[key] > 0:
        print(key, "->", alphaCount[key])