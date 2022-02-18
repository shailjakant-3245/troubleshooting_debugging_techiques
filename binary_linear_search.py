#!/usr/bin/env python3

import generate_list
import sys

list = generate_list.alphabet()
ind = sys.argv   #index no. to be searched
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

print(binary_search(list,key))



def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

print(linear_search(list,key))