"""

Write a recursive method named sumArray
public static int sumArray(int[] a, int left, int right)
Returns the sum of all values between left and right in the array a

"""


def sumArray(a, left, right):


    if left == right :
        return a[right]
    else:
        return (a[left] + sumArray(a, left+1, right))



if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    print(sumArray(a, 0, 5))
