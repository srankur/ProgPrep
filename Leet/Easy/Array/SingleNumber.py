"""

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""


# Method-1: Brute Logic

def singleNumber(nums):
    for i in range (len(nums)):
        for j in range( len(nums)):
            if i != j and nums[i] == nums[j] :
                break
            elif j == len(nums) -1:
                print("Unique", nums[i])


# Method-2: Using a counter of elements
def singleNumber_1(nums):
    unique = {}
    for i in range(len(nums)):
        if nums[i] in unique:
            unique[nums[i]] = unique[nums[i]] + 1
        else:
            unique[nums[i]] = 1

    for k,v, in unique.items():
        if v == 1:
            return k


# Method-3: Using XOR for SINGLE unique number in array
# 2^3^2 = {2^2)^3 = 0^3 = 3
def singleNumber_2(nums):
    number = 0
    for x in nums:
        number = number^x
    return number


if __name__ == "__main__":
    nums = [1,2,1,2,3]
    singleNumber(nums)
    print("singleNumber_1: ", singleNumber_1(nums))
    print("singleNumber_2: ", singleNumber_2(nums))



