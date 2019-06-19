"""
Write a recursive method named onlyPositive
public static boolean onlyPositive(int[] a, int left, int right)

Returns true if all values between left and right in the array a are positive
Otherwise, returns false

"""



def onlyPositive(a, left, right):

    if left == right and a[left] >= 0:
        return True
    elif left == right and a[left] < 0:
        return False

    if a[left] >= 0 and onlyPositive(a, left+1, right):
        return True
    else:
        return False


if __name__ == "__main__":
    a = [1, 2, 3, 4, -1, 4, 5]
    print(onlyPositive(a, 5, 6))