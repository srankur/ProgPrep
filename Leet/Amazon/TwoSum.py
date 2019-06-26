"""

 Two Sum
  Go to Discuss
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

"""
Questions: 
1- is array aorted ? use two pointer concept. 
2- Array is not sorted, May use dictoinary/set to check the match.  
3- Number in the array are unique ? 

"""

# Approach-1: naive
def TwoSumNaive(num_list, target):
    for i in range (len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                return i,j


#Approach-2
def TwoSum_sortedArray(num_list, target):
    high = len(num_list) -1
    low = 0

    while low < high:
        if num_list[low] + num_list[high]  == target:
            return low, high
        elif num_list[low] + num_list[high] > target:
            high -= 1
        elif num_list[low] + num_list[high] < target:
            low += 1


#Approach-3

def TwoSum_Set(num_list, target):
    check_set = {}
    for i in range(len(num_list)):
        if target - num_list[i] not in check_set:
            check_set[num_list[i]] = i
        if target - num_list[i] in check_set:
            return i , check_set[target - num_list[i]]



# Driver Code
if __name__ == "__main__":
    arr = [5, 2,3,12, 7]
    result = TwoSumNaive(arr, 12)
    print ("Indices = > ", result)


    arr = [ 2,3, 7, 9 ]
    result = TwoSum_sortedArray(arr, 10)
    print ("Indices = > ", result)


    arr = [5, 2,3,12, 7]
    result = TwoSum_Set(arr, 12)
    print ("Indices = > ", result)