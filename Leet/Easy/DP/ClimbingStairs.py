"""

Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

import time

# Approach-1:
#

def TopDownRecursion(n):

    # Base Case 1: return 0 if number is negative
    if (n < 0):
        return 0

    # Base Case 2: return 0 if number is negative
    if n == 0:
        return 1

    return TopDownRecursion(n-1) + TopDownRecursion(n-2)

Memo = {}

def TopDownRecursionMemoization(n):
    if n not in Memo.keys():
        Memo[n] = TopDownRecursionMemoHelper (n)
    return Memo[n]

def TopDownRecursionMemoHelper(n):

    # Base Case 1: return 0 if number is negative
    if (n < 0):
        return 0

    # Base Case 2: return 0 if number is negative
    if n == 0 :
        return 1

    firstPart = TopDownRecursionMemoization(n-1)
    secondPart = TopDownRecursionMemoization(n-2)

    print(firstPart, secondPart)

    return (firstPart + secondPart)





# Driver Code

if __name__ == "__main__":
    start = time.time()
    #print(TopDownRecursion(40), time.time() - start)

    print(TopDownRecursionMemoization(6), time.time() - start)
