import math
import time
from datetime import timedelta

from timeit import default_timer as timer

x = 1
start = time.time()
factor = 100_000
for j in range(1, 7):
        factor *=j
        for i in range(0,factor):
                x += 1
        end = time.time()
        print(round(end - start,3))


x = 1
start = timer()
factor = 100_000
for j in range(1, 7):
        factor *=j
        for i in range(0,factor):
                x += 1
        end = timer()
        print(timedelta(seconds=end-start))