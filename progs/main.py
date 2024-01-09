from sys import path

path.append("C:\\Users\\obele\\Programming\\Python\\PE2_mod1.3.2\\modules")

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))