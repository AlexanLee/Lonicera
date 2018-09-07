
import sys
from random import random

n = int(sys.argv[1])

for i in range(n):
    x = 2 * random() - 1.0
    y = 2 * random() - 1.0
    label = 1
    if abs(x) + abs(y) < 1.0:
        label = 0
    fx = "x" + str(int(x*10)) + ":1"
    fy = "y" + str(int(y*10)) + ":1"
    print str(label) + " " + fx + " " + fy

