"""
Implement strStr()


Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().
"""


'''
Naive Approach:
- Loop for haystack need to run (Source String -Substring) times, Why ??
    - To Avoid the out of bound exception, In one of the worst case Substring may be the 
    last characters of Source String. e.g. 
    - SourceString = "Hello World!!" , SubString = "World!!"
 
'''

def StrStr_naive(pattern, text):
    m = len(text)
    n = len(pattern)

    if m is None or n is None:
        return -1

    if m < n:
        return -1

    for i in range (m - n +1 ): # m - n + 1 to avoid the boundary
        j = 0
        for j in range(n):
            if text[i+j] != pattern[j]:
                break

            if j == n-1: # J value traversed the entire pattern
                return i

    if m > m-n: #pattern Not found
        return -1


# Driver Code

if __name__ == "__main__":
    text = "Hello"
    pattern = "lo"

    print(StrStr_naive(pattern, text))

