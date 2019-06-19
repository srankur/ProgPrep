"""
Write a recursive method named countChar
public static int countChar(String str, char c)

Returns a count of number of times character c occurs in String str

"""


def countChar(str, char):
    strlen = len(str) -1

    count = countCharHelper(str, strlen, char)
    return count




def countCharHelper(str, strlen, char):
    count = 0

    if str is None:
        return 0

    if strlen == 0 and str[strlen] == char:
        return 1

    if str[strlen] == char:
        count = countCharHelper(str, strlen -1, char)
        count += 1
    else:
        count += countCharHelper(str, strlen -1, char)

    return count

if __name__ == "__main__":
    str = "aacdcb"

    print(countChar(str, 'a'))