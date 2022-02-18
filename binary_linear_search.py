#!/usr/bin/env python3

import generate_list
import sys
import time

begin = time.time()
list = generate_list.alphabet()
end= time.time()
print("TIme taken for list generation : {}".format(end-begin))


ind = int(sys.argv[1])   #index no. to be searched
key = list[ind]   #"zzz999" #  sys.argv
print("Size of list is: "+str(len(list)))


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

begin= time.time()

print(binary_search(list,key))

end = time.time()
print("TIme taken for execution of binary search : {}".format(end-begin))

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1
begin= time.time()

print(linear_search(list,key))

end = time.time()
print("TIme taken for execution of linear search : {}".format(end-begin))