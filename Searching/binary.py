#python program to do binary search using Recursion
import math
def bin(li, l, h, x):
    if h >= l:
        mid = l + (h - l)//2
        if li[mid] == x:
            return mid
        elif li[mid] > x:
            return bin(li, l, mid-1, x)
        else:
            return bin(li, mid+1, h, x)
    else:
        return -1
li = [20, 21, 22, 23, 24]
x = int(input("enter the number: "))
res = bin(li, 0, len(li)-1, x)
if res != -1:
    print("the value is at position: ", str(res))
else:
    print("Value not found!!")
