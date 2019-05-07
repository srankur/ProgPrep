
"""

Problem:
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new
length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
extra memory.



"""
#nums = [0,0,1,1,1,2,2,3,3,4]
###
# i=0, j=0 [0,0,1,1,1,2,2,3,3,4] j: 0->0
# i=1, j=0 [0,1,1,1,1,2,2,3,3,4] j: 0->1
# i=2, j=1 [0,1,1,1,1,2,2,3,3,4] j: 0->1
# i=3, j=1 [0,1,1,1,1,2,2,3,3,4] j: 0->1
# i=4, j=1 [0,1,2,1,1,2,2,3,3,4] j: 1->2
# i=5, j=2 [0,1,2,1,1,2,2,3,3,4] j: 1->2
# i=6, j=2 [0,1,2,3,1,2,2,3,3,4] j: 2->3
# i=7, j=3 [0,1,2,3,1,2,2,3,3,4] j: 2->3
# i=8, j=3 [0,1,2,3,4,2,2,3,3,4] j: 3->4

import time

def removeDuplicates( nums):
    if len(nums) < 2:
        return
    j = 0
    for i in range(len(nums) - 1):
        print("Outer:)nums[%s]: %s, nums[%s]: %s " % (i, nums[i], i+1, nums[i+1]))
        if nums[i] != nums[i + 1]:
            j += 1
            nums[j] = nums[i + 1]
            print("Inner: nums[%s]: %s, nums[%s]: %s " % (j, nums[j], i + 1, nums[i + 1]))
    return j + 1  # since j starts with zero, actual length will be "+1" to the current value




# Approach:

def removeDuplicates_sortedArray(arr):
    length = len(arr)
    #Case1: Array is too small to compare
    if length is None or length < 2 :
        return length

    j = 0
    for i in range(0, length -1): # one less of the length to avoid out of bound index.
        if arr[i] != arr[i+1]:
            j += 1
            arr[j] = arr[i+1]
    return j+1 # returning j+1: because J was initialized to zero.



if __name__ == "__main__":
    start = time.time()
    #Create a list of inputs
    nums = [
        [],
        [1,1],
        [-1, 1],
        [1,1,2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [0] * 10000
        ]

    print(list(map(removeDuplicates_sortedArray, nums)), time.time() - start)
