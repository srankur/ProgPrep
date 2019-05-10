"""

Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"""




def reverseInteger_iterative_simple(num):
    rev = 0
    negative_flag = False

    if num < 0:
        negative_flag = True
        num = -num
    while num > 0:
        temp = num % 10
        rev = rev * 10 + temp
        num = num // 10
    if num > 2**31:
        print("Number Overflowed!!")
        num = 0

    if num < -2**31:
        print("Number underlowed!!")
        num = 0

    return -rev if negative_flag == True else rev


# DriverCode

if __name__ == "__main__":
    num = -123
    num = 983475894679847698379879875938759348756984376984576983457698347689437698436843798673489673498673498763498763948

    print(reverseInteger_iterative_simple(num))

