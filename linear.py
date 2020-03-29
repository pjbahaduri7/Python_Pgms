import math
def lin(li, ele):
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return print("Invalid")
li = [10, 20, 30, 40]
item = int(input("Enter the item: "))
print("position: ", lin(li, item))