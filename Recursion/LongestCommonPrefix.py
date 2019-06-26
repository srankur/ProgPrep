"""
Longest Common Prefix using Divide and Conquer Algorithm
Given a set of strings, find the longest common prefix.
Examples:

Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output : "gee"

Input  : {"apple", "ape", "april"}
Output : "ap"


"""



#
"""
approach -1 : Divide and conquer
                            “geeksforgeeks”, “geeks”, “geek”, “geezer”
                            /                                        \
                “geeksforgeeks”, “geeks”,                           “geek”, “geezer”
                /                       \                             /            \
        “geeksforgeeks”,                “geeks”                 “geek”,            “geezer”
        LCP = geeks                                                 LCP = gee

Time Complexity : Since we are iterating through all the characters of all the strings, so we can say that the time complexity is O(N M) where,

N = Number of strings
M = Length of the largest string string
Auxiliary Space : To store the longest prefix string we are allocating space which is O(M Log N).

"""

def commonPrefixUtil(str1, str2):
    print ("Received- 1: {}, 2: {}".format(str1, str2))

    str1_len = len(str1)
    str2_len = len(str2)
    i = 0
    j = 0
    result = ""
    # run a loop while a string
    while i < str1_len and j < str2_len:
        if str1[i] == str2[j]:
            result += str1[i]
            i +=1
            j +=1
        else:
            break
    return result



def commonPrefix(str_list, low , high):

    if low == high:
        return str_list[low]

    if high > low:
        # Same as low + high /2 , but to avoid overflow where large number of high/low/high + low
        mid = low + (high - low)//2

        str1 = commonPrefix(str_list, low , mid)
        str2 = commonPrefix(str_list, mid +1 , high)
        print("Str1: {}, Str2: {}".format(str1, str2 ))
        return commonPrefixUtil(str1, str2)


"""
Approach-2: Word by word matching 

LCP(string1, string2, string3) = LCP (LCP (string1, string2), string3)

Like here

LCP (“geeksforgeeks”, “geeks”, “geek”)  =  LCP (LCP (“geeksforgeeks”, “geeks”), “geek”)
                                        =  LCP (“geeks”, “geek”) = “geek”


Time complexity- iterating through all the strings and for each string we are iterating though each characters, 
    so we can say that the time complexity is O(N M) where,
        N = Number of strings
        M = Length of the largest string string 

"""


def commonPrefix_Associative(str_list):
    prefix = str_list[0]
    for i in range (1, len (str_list)):
        prefix = commonPrefixUtil(prefix, str_list[i])
    return prefix




"""
Approach-3rd :Character by Character Matching

arr = [ "g e e k sforgeeks", 
        "g e e ks",
        "g e e k", 
        "g e e zer"]
 
"""




# Driver code

if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks",
           "geek", "geezer"]

    n = len(arr)
    #ans = commonPrefix(arr, 0, n - 1)
    ans = commonPrefix_Associative(arr)
    if len(ans):
        print("The longest common prefix is", ans)
    else:
        print("There is no common prefix")