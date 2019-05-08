"""
Plus One
  Go to Discuss
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.


"""


# Approach
'''
Case#1: when 
Input: 123, Initial Carry = 1
Carry   item    resultant_array
1       3       [1,2,4]
0       2       [1,2,4]
0       1       [1,2,4]

Input: 999
Carry   item    resultant_array
1       9       [9,9,0]
1       9       [9,0,0]
1       9       [0,0,0]
Need to copy array in with additional carry


'''

def plusOne(digits):
    carry = 1 # Need to ass one.
    output = []
    len_Of_digits = len(digits)

    for  i in range(len_Of_digits -1 ,-1 , -1):
        newValue= (digits[i] + carry) %10
        carry = int((digits[i] + carry) // 10)
        digits[i] = newValue

    if carry:
        output.append(carry)
        return(output + digits)

    return digits



# Driver Code
if __name__ == "__main__":
    input = [
        [],
        [9],
        [1,2,3],
        [9,9,9,9]
    ]
    output = list(map(plusOne, input))
    print(output, sep="\n")




