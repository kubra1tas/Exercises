#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#



def findSubstring(s, k):
    coutner = 0
    coutner2 = 0
    tmp = 0
    for count in range(len(s)):
        word = s[int(count): int(count) + int(k)]
        if len(word) < k:
            break
        for x in word:
            if (x == 'a' or x == 'e' or x == 'i' or
                    x == 'o' or x == 'u'):
                coutner += 1
            coutner2 += coutner
        if coutner > tmp:
            final = word
            tmp = coutner
        coutner = 0

    if coutner2 == 0:
        return("Not found!")

    return str(final)




if __name__ == '__main__':

    s = input()

    k = int(input().strip())

    result = solve(s, k)


