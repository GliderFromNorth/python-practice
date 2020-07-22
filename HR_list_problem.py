# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
l = []
for n in range(int(input("Enter Number of Iterations:"))):
    c = input("Enter your command with proper attribute:").split()
    try:cmd, position0, position1 = c[0],c[1],c[2]
    except: cmd, position0 = c[0],c[1]
    if cmd == "insert":l.insert(int(position0),int(position1))
    if cmd == "print" :print(l)
    if cmd == "remove":l.remove(int(position0))
    if cmd == "append":l.append(int(position0))
    if cmd == "sort"  :l.sort()
    if cmd == "pop"   :l.pop()
    if cmd == "reverse": l.reverse()
print(l)