#!/usr/bin/env python3
from os import strerror

alphaCount = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

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