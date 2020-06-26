# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 06:55:12 2020

@author: jhasa
"""


sally = "sally sells sea shells by the sea shore"
characters ={}
for x in sally:
    if x not in characters:
        characters[x] = 0
    characters[x] = characters[x] +1
maxx = [x for x in characters.values()]
print(maxx)
for k in characters:
    if (characters[k]) == max(maxx):
        max_value = k 
        print(max_value, characters[k] )