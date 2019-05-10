"""

Valid Anagram:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


def validAnagrams_naive(s, t):
    s= sorted(s)
    t = sorted(t)

    if s == t:
        return True
    return False


def validAnagrams_opti(s, t):
    pass



# DriverCode

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    print(validAnagrams(s,t))