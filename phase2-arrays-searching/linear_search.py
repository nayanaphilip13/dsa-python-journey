#Data Structure -> A data structure is just a smart way to organize your data so you can use it efficiently.
#ex: Array/List, Stack, Queue, Tree, Dictionary, Graph
# Algorithm -> An algorithm is just a set of steps to solve a problem.

# 1. Arrays + Searching
# Problem — Find a number in a list
# List:  [64, 34, 25, 12, 22, 11, 90]
# Find:  25
# How would YOU find 25 in this list if you were doing it manually?
# You'd probably start from the first number, check one by one... right?
# That method has a name — it's called Linear Search!
def number_search(list, target):
    for i in range(len(list)):
        if(list[i] == target):
            print(target, "found in", i, "position")
            return
    print(target, "not found")
list = [64, 34, 25, 12, 22, 11, 90]
number_search(list, 25)
number_search(list, 99)
            
# If the list had 100 numbers and the target was at position 99 — how many checks would the computer have to make?
# 100 Checks
# If the target was at position 0 — how many checks? 1 Check
# What is the worst case — maximum checks it will ever need? n checks

# BIG O
# Best case  → 1 check      → O(1)
# Worst case → n checks     → O(n)

# O(1) = 1 check = instant
# O(n) = n checks = grows with list size

# That's literally what Big-O means.