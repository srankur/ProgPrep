"""

Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


def isValidPalindrome(arr):
    newarr = arr.lower()
    i = 0
    j = len(newarr) - 1
    while i < j:
        while 'a' > newarr[i] or newarr[i]  > 'z':
            i += 1
        while 'a' > newarr[j] or  newarr[j] > 'z':
            j -= 1

        if newarr[i] != newarr[j]:
            return False

        i += 1
        j -= 1

    return True



# DriverCode
if __name__ == "__main__":
    input = [
        "",
        "race a car",
        "A man, a plan, a canal: Panama",
    ]

    print (list(map(isValidPalindrome,input)))
