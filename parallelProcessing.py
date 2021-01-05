#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    # Write your code here
    totalTime = 0
    new = []
    for item in files:
        if item % numCores == 0:
            new.append([item, item/numCores])

    asd = []
    for i in range(limit):
        asd.append(max(new))
        files.remove(max(new)[0])
        new.remove(max(new))

        if len(new) == 0:
            break


    for item in files:
        totalTime += item

    for i in range(limit):
        totalTime = totalTime + max(asd)[1]
        asd.remove(max(asd))
        if len(asd) == 0:
            break


    return int(totalTime)

if __name__ == '__main__':

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)
    print(result)

