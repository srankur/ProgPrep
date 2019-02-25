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


def removeDuplicates(self, nums: 'List[int]') -> 'int':
    if len(nums) < 2:
        return
    j = 0
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            j += 1
            nums[j] = nums[i + 1]
    return j + 1  # since j starts with zero, actual length will be "+1" to the current value