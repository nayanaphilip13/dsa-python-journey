# List:
# Index: 0    1    2    3    4    5    6
# Value:[5,  11,  22,  34,  64,  78,  90]

# Your brain says:
# "78 is a big number...
# so it's probably towards the RIGHT side...
# no need to check 5, 11, 22 at all!"

# That instinct is Binary Search!

# How Binary Search actually works

# Instead of starting from left — we start from the MIDDLE!

# Step 1 — Find the middle

# [5,  11,  22,  34,  64,  78,  90]
#                 👆
#              middle = 34

# Step 2 — Is 34 == 78?

# No!
# Is 78 > 34? YES!
# So 78 must be on the RIGHT side!
# Forget the left side completely! 🗑️

# Step 3 — Now only look at right side

# [64,  78,  90]
#        👆
#     middle = 78

# Step 4 — Is 78 == 78?

# YES! Found it! 🎉
# See how fast that was? 👇
# Linear Search  → checked 6 boxes to find 78
# Binary Search  → checked only 2 boxes!

# With 1000 numbers?

# Linear Search  → worst case 1000 checks 😩
# Binary Search  → worst case only 10 checks! 😎

# That's the power of Binary Search! 🔥

# The only rule — list MUST be sorted!
# ✅ [5, 11, 22, 34, 64, 78, 90]  → Binary Search works!
# ❌ [34, 5, 90, 11, 22]          → Binary Search won't work!

# If list is unsorted → use Linear Search
# If list is sorted → always use Binary Search ✅

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if(numbers[middle] == target):
            print(target, "is found in ", middle, "index")
            return
        elif numbers[middle] < target:
            left = middle + 1    # ignore left side, move right

        else:
            right = middle - 1   # ignore right side, move left

    print(target, "not found")

numbers = ([5, 11, 22, 34, 64, 78, 90], 22)
binary_search(numbers, 78)
binary_search(numbers, 100)
# // means divide and remove decimal:
# (0+6)//2 = 3  ✅
# (0+6)/2  = 3.0 ← we don't want decimal for index

# Change target to 5 — how many checks does it take? trace it step by step like I did above -> 3 checks
# List: [5,  11,  22,  34,  64,  78,  90]
# Index: 0    1    2    3    4    5    6

# Round 1:
# left=0, right=6
# middle = (0+6)//2 = 3 → numbers[3] = 34
# 5 < 34 → ignore RIGHT side
# right = middle-1 = 2
#                         ✅ Check 1

# Round 2:
# left=0, right=2
# middle = (0+2)//2 = 1 → numbers[1] = 11
# 5 < 11 → ignore RIGHT side
# right = middle-1 = 0
#                         ✅ Check 2

# Round 3:
# left=0, right=0
# middle = (0+0)//2 = 0 → numbers[0] = 5
# 5 == 5 → FOUND at index 0! 🎉
#                         ✅ Check 3
# Change target to 100 — what prints? 
# Target Not found in list
# What happens if you run binary_search([5, 11, 22, 34, 64, 78, 90], 22)?

# Round 1:
# left=0, right=6
# middle=3 → numbers[3]=34
# 22 < 34 → ignore right side
# right = 2
#                         ✅ Check 1

# Round 2:
# left=0, right=2
# middle=1 → numbers[1]=11
# 22 > 11 → ignore left side
# left = 2
#                         ✅ Check 2

# Round 3:
# left=2, right=2
# middle=2 → numbers[2]=22
# 22 == 22 → FOUND at index 2! 🎉
#                         ✅ Check 3

# Write a function called binary_search_count that:

# Does binary search
# Also counts how many checks it made
# Prints the count at the end

# Expected output:

# Found 78 at index 5
# Total checks made: 2


def binary_search_count(numbers, target):
    left = 0
    right = len(numbers) - 1
    count = 0          # add this to count checks

    while left <= right:
        count += 1     # every loop = one check
        middle = (left + right) // 2
        if numbers[middle] == target:
            print("Found", target, "at index", middle)
            print("Total checks made:", count)
            return
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    print(target, "Not Found")
    print("Total checks made:", count)


numbers = [5, 11, 22, 34, 64, 78, 90]
binary_search_count(numbers, 78)
binary_search_count(numbers, 5)
binary_search_count(numbers, 22)
binary_search_count(numbers, 100)
