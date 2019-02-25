"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true


"""


# Method-1: brute Force:
# Step-1: pick one element and search for it in the array
# O(n*2)
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False



# With O(n) extra space
def containsDuplicate_1(nums):
    containdups = set()
    for x in nums:
        if x in containdups:
            return True
        else:
            containdups.add(x)
    return False





if __name__== "__main__":

    print(containsDuplicate([1,2,2,1]))
    print(containsDuplicate_1([1,1]))




