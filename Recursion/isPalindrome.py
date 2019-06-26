"""
Write a recursive method named isPalindrome
public static boolean isPalindrome(String str)
Returns true if the String str is a palindrome
Otherwise, returns false

"""

def isPalindrome(str):
    strlen = len(str)

    result = isPalindromeHelper(str, 0, strlen-1)
    return result

def isPalindromeHelper(str, left, right):

    if left == right:
        return True

    if left > right:
        return True

    return str[left] == str[right] and isPalindromeHelper(str, left+1 , right -1)


if __name__ == "__main__":
    str = "abcdba"

    print(isPalindrome(str))
