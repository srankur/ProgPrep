"""

Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


def MoveZeroes(arr):
    j = 0

    for i in range(len(arr)):
        if arr [i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr


if __name__ == "__main__":
    input = [
        [],
        [0, 1, 0, 3, 12],
        [0,0,0,0,0],
        [1,0,1,0,1,0,1,0]
    ]
    result = list(map(MoveZeroes, input))
    print (result)

