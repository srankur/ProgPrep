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

from collections import Counter

def validAnagrams_naive(s, t):
    s= sorted(s)
    t = sorted(t)

    if s == t:
        return True
    return False


def validAnagrams_opti(s, t):
    # Make a couter dictionary of source string
    source_cnt = Counter(s)
    print(source_cnt)
    # iterate through the target string,
    # check for the item in source counter
    # Deduct the count if available

    for i in range(len(t)):
        if t[i] in source_cnt:
            source_cnt[t[i]] -= 1
            if source_cnt[t[i]] == 0:
                del source_cnt[t[i]]
    print(source_cnt)
    return False if (len(source_cnt) > 0) else True






# DriverCode

if __name__ == "__main__":
    s = "anagramr"
    t = "nagaram"

    #print(validAnagrams_naive(s,t))
    print(validAnagrams_opti(s,t))