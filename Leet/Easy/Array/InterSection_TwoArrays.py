"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


"""

def intersection_unsorted_method_1(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    intersection = []
    i = 0
    j = 0
    while (i < m and j < n ):
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            intersection.append(arr1[i])
            i += 1
            j += 1
    return intersection


def intersection_unsorted_method_2(arr1, arr2):
    pass




# Driver code
if __name__ == "__main__":
    input1 = [0, 1,2,2,3,7,8]
    input2 = [2,2,7]

    print(intersection_unsorted_method_1(input1, input2))