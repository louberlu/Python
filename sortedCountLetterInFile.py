#!/usr/bin/env python3
from os import strerror
from operator import itemgetter

alphaCount = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

filename = input("Enter the file's name: ")
try:
    file = open(filename, 'rt')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)

content = file.read()
for char in content:
    if char.isalpha():
        alphaCount[char.lower()]+=1
 
# Sort by value
sortDict = dict(sorted(alphaCount.items(), key=itemgetter(1), reverse= True))

dstname = filename.replace('.txt', '.hist')
try:
    dst = open(dstname, 'wt')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    file.close()
    exit(e.errno)	

for key in sortDict.keys():
    line = key + "->" + str(sortDict[key])+"\n"
    dst.write(line)
    if sortDict[key] > 0:
        print(line)

file.close()
dst.close()