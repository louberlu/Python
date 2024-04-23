from multiprocessing import Pool
from multiprocessing import Process, current_process
import time
from time import sleep
import random

def pg1():
    for i in range(0,6):
        j = 1
        while j <= 5 and j >=1:
            j+=1
        print("pg1")

def pg2():
    for i in range(0,6):
        j = 1
        while j <= 5 and j >=1:
            j+=1
        print("pg2")

if __name__ == "__main__":
    pool = Pool(processes=2)
    result = pool.apply_async(pg1)
    print(result.get(2))
    pg2()