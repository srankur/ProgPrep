"""

Write a program to calculate pow(x,n)
Given two integers x and n, write a function to compute xn. We may assume that x and n are small and overflow doesn’t happen.

Examples :

Input : x = 2, n = 3
Output : 8

Input : x = 7, n = 2
Output : 49
"""

# approach-1 : Divide the power by 2 if power is even
# Complexity : Time- O(n) and space- O(1) if space calculated as 1
def PowerofX_divide_PowerByTwo(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return PowerofX_divide_PowerByTwo(x, n//2) * PowerofX_divide_PowerByTwo(x, n//2)
    else:
        return x * PowerofX_divide_PowerByTwo(x, n//2) * PowerofX_divide_PowerByTwo(x, n//2)


# approach-1 : Divide the power by 2 and calculate it once
# Complexity : Time- O(logn) and space- O(1) if space calculated as 1

def PowerofX_CalculatePower(x,n):
    if n == 0:
        return 1
    print("Pusshing n as  : ", n//2)
    temp = PowerofX_CalculatePower(x, n//2)
    print("Temp = {} for n = {}".format(temp,n//2))
    if n % 2 == 0:
        return temp * temp
    else:
        return x* temp * temp


# For a negative power of a flating point number

def PowerofX_NegativePower(x,n):
    if n == 0:
        return 1
    temp = PowerofX_NegativePower(x, n/2 )

    if n % 2 == 0:
        return temp * temp
    else:
        if n > 0:
            return x * temp * temp
        else:
            return ((temp * temp)/x)



if __name__ == "__main__":
    #print(PowerofX_divide_PowerByTwo( 5, 4))
    #print(PowerofX_CalculatePower(5, 3))
    print(PowerofX_NegativePower(5, -3))