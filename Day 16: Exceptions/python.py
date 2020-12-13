#!/bin/python3

import sys


S = input().strip()

try:
    a = int(S)
    print(a)
except ValueError:
    print("Bad String")
    
