import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bn=list(bin(n))
    bn=bn[2:]

    count=0
    maxx=0

    for i in range(len(bn)):
        if bn[i]=='1':
            count+=1
        else :
            if maxx<count:
                maxx=count
            count=0
   