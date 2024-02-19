#!/usr/bin/env python3

try:
    stream = open("C:\\Users\\Karen\\testStreamPython.txt", "r")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)

