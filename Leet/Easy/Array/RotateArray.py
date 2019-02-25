"""

Problem: Given an array, rotate the array to the right by k steps, where k is non-negative.

Example-1

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Example-2
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""


# Method_1: Rotate one element at a time
# Step#1:  Pick first element save in temp
# Step#2: shift all other element by one index to the left.
#

def rotate_1(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) > 1:
        newK = k
        if k > len(nums):
            newK = k % len(nums)
        for i in range (newK):
            temp = nums[0]
            for j in range(1, len(nums)):
                nums [j-1] = nums [j]
            nums[len(nums) -1 ] = temp
    print (nums)


# Method:2 block of array to shift
# Method3: GCD of Length and K

# Method4 :  Reverse of the array

def arrayreverse(arr):
    i = 0
    j = len(arr)
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]

def rotate_4(arr, k):
    shift = k;
    if k > len(arr):
        shift = k % len(arr)


    reversed(arr[:shift])
    reversed(arr[shift:])
    reversed(arr)

    print(arr)


if __name__ == "__main__":


    nums = [1,2,3,4,5,6,7]
    k = 100000000
    rotate_1(nums,k)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    rotate_4(nums,k)