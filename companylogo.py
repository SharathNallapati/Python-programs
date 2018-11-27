#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    from collections import Counter
    s= Counter(input()).items()
    s=sorted(s,key=lambda s:s[0])

    for i in sorted(s,key=lambda s:s[1],reverse=True)[:3]:
       print(" ".join(map(str,i)))
