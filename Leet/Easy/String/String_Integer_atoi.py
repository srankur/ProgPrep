"""
String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is
found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2**31,  2**31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN
(−231) is returned.

Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

"""

# -42
def atoi(arr):
    negative_flag = False
    base = 10
    num = 0

    for i in range(len(arr)):
        if arr[i] == " ":
            i += 1
            continue

        # Negative sign check
        if arr[i] == "-":
            negative_flag = True
            i += 1
            continue

        # Postive sign check
        elif arr[i] == "+":
            i += 1
            continue

        # range check
        if ord("0") <= ord(arr[i]) <= ord("9"):
            num = (num * base) + (ord(arr[i] ) - ord('0'))
            #base = base*10
            if num > 2**31:
                return 2**31 -1
            elif num < 2**31 and negative_flag == True:
                return -2**31

        elif ord(arr[i]) < 0 or ord(arr[i]) > 9:
            break

    return -num if (negative_flag == True) else num




# Driver Code
if __name__ == "__main__":
    num = "          -4267707870"
    print(atoi(num))