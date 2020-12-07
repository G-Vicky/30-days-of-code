#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = "{0:b}".format(n)
    
    maxConcurrent = count = 0
    for i in binary:
        if i == '1':
            count += 1
        else:
            count = 0
        if count > maxConcurrent:
            maxConcurrent = count
    
    print(maxConcurrent)

