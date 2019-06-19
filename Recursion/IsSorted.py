"""

Write a recursive method named isSorted
public static boolean isSorted(int[] a, int left, int right)
Returns true if all values between left and right in the array a are in increasing order

"""

def isSorted(a, left, right):

    if left == right:
        return True

    if len(a) == 0:
        return True

    return a[left] < a[left +1] and isSorted(a, left+1, right)



if __name__ == "__main__":
    a = [1,2,3,4,5, 2,1]

    print(isSorted(a,5, 6 ))