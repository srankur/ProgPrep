"""

Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# Possible queries-
# Is array sorted ?
# does it have a repeated element- Result in dictionary error


def twoSum_Naive(arr, sum):
    length = len(arr)

    for i in range (length):
        for j in range(i+1 , length ):
            if arr[i] + arr[j] == sum:
                return i,j
    return None



def twoSum_SortedArray_twoPointers(arr, sum):
    i = 0
    j = len(arr) -1

    while i < j:
        if arr[i] + arr [j] == sum:
            return i,j
        elif arr[i] + arr [j] > sum:
            j -= 1
        elif arr[i] + arr[j] < sum:
            i += 1
    return None



def twoSum_unsorted_map(arr, sum):
    check = {}

    for i in range (len(arr)):
        if (sum - arr[i]) not in check:
            check[arr[i]] = i
        elif arr[i] + arr [check[sum - arr[i]]]  == sum:
            return  check[sum - arr[i]], i


    return None





# Driver Code
if __name__ == "__main__":
    input = [2, 7, 11, 15]
    sum_list = [9,13, 15]

    func_list = [
        twoSum_Naive,
        twoSum_SortedArray_twoPointers,
        twoSum_unsorted_map
    ]



    print(twoSum_Naive(input, 17))
    print(twoSum_SortedArray_twoPointers(input, 9))
    print(twoSum_unsorted_map(input, 9))