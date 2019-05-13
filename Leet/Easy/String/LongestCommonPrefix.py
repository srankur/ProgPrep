"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""


"""
Approach-1 Horizontol Scanning
Intuition

For a start we will describe a simple way of finding the longest prefix shared by a set of strings LCP(S_1 \ldots S_n)
LCP(S1…Sn). We will use the observation that :

LCP(S_1 \ldots S_n) = LCP(LCP(LCP(S_1, S_2),S_3),\ldots S_n)LCP(S1…Sn)=LCP(LCP(LCP(S1,S2),S3),…Sn)

Algorithm

To employ this idea, the algorithm iterates through the strings [S_1 \ldots S_n][S1…Sn], finding at each iteration ii 
the longest common prefix of strings LCP(S_1 \ldots S_i)LCP(S1…Si) When LCP(S_1 \ldots S_i)LCP(S1…Si) is an empty string
, the algorithm ends. Otherwise after nn iterations, the algorithm returns LCP(S_1 \ldots S_n)LCP(S1…Sn).

Time complexity : O(S)O(S) , where S is the sum of all characters in all strings.
In the worst case all n strings are the same. The algorithm compares the string S1 with the other strings 
[S2…Sn] There are S character comparisons, where S is the sum of all characters in the input array.

Space complexity : O(1). We only used constant extra space. 

"""

class Solution:
    def longestCommonPrefix_horizontalScanning(self, strs): # Strs is list of strings
        # Retuen empty string if Strs is None or the length is zero.
        if strs is None or len(strs) == 0:
            return None

        #initialize LCP with the first string itself
        LCP = strs[0]

        #start scanning the list with ist string onwards
        for i in range(1,len(strs)):
            current_word = strs[i]
            print("Current LCP: %s \tCurrent Word: %s " % (LCP, current_word))
            j = 0
            # traversed value of j is the index of common prefix for string and LCP
            for j in range(min(len(LCP), len(current_word))):
                print("Comparing:  %s with %s" % (current_word[j], LCP[j]))
                if current_word[j] != LCP[j]:
                    j -= 1 #decreasing the J to correct the new LCP value
                    break
            LCP = LCP[0:j+1] # j+1 to accomodate the last char
        return None if len(LCP) == 0 else LCP


    def longestCommonPrefix_verticalScanning(self, strs):

        if strs is None or len(strs) == 0:
            return None

        # Assigning first word as LCP
        LCP = ""

        # Outer loop for the length of LCP
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for j in range (1, len(strs)):
                word = strs[j]
                if len(word) <= i or word[i] != current_char:
                    return LCP
            LCP += current_char




# Driver Code
if __name__ == "__main__":
    Input_1 = ["flower","flow","flight"]
    Input_2 =  ["dog", "racecar", "car"]
    Input_3 = []
    Input_4 = None

    LCP = Solution()
    print(LCP.longestCommonPrefix_horizontalScanning(Input_1))
    print(LCP.longestCommonPrefix_horizontalScanning(Input_2))
    print(LCP.longestCommonPrefix_horizontalScanning(Input_3))
    print(LCP.longestCommonPrefix_horizontalScanning(Input_4))

    print(LCP.longestCommonPrefix_verticalScanning(Input_1))
    print(LCP.longestCommonPrefix_verticalScanning(Input_2))
    print(LCP.longestCommonPrefix_verticalScanning(Input_3))
    print(LCP.longestCommonPrefix_verticalScanning(Input_4))

