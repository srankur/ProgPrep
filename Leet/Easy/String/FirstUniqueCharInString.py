"""

First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
from collections import Counter

def non_repeat_char_index_naive(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if i != j and arr[i]== arr[j]:
                count += 1
        if count == 0:
            return i
            break
    return -1


def non_repeat_char_using_Python_collections(arr):
    char_count = Counter(arr)
    for i in range(len(arr)):
        if char_count[arr[i]] == 1:
            return i
    return -1



# Driver Code
if __name__ == "__main__":
    input = [
        "",
        "aabb",
        "leetcode",
        "loveleetcode"
    ]

    func_list = [
        non_repeat_char_index_naive,
        non_repeat_char_using_Python_collections
    ]

    result = [list(map (x,input)) for x in func_list]
    print(result)
