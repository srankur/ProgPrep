"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


# Method-1: Valley and Peak approach
# Calculate consecutive valleys and peak
# Add to the max Profit


def maxProfit_1(prices):

    if (len(prices) < 2):
        return 0

    if (len(prices) > 2):
        price_peak = prices[0]
        price_valley = prices[0]

    profit = 0
    i = 0
    while i < len(prices) -1:
        while i < len(prices) -1 and prices[i] >= prices[i+1]:
            i += 1
        price_valley = prices[i]

        while i < len(prices) -1 and prices[i] < prices[i+1]:
            i += 1
        price_peak = prices[i]

        profit =  price_peak - price_valley
        return profit


# Method-2: Valley and Peak approach for each transaction
# Calculate consecutive valleys and peak
# Add to the max Profit

def maxProfit_2(prices):
    profit = 0
    for i in range (1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit


def maxProfit_non_valleypeak(arr):
    profit = 0
    j = 0
    length= len (arr)
    for i in range(length):
        j = i + 1 # Keep the j, one pointer ahead of i
        if j < length and arr[i] > arr[j]:
            continue

        if j < length and arr[i] < arr[j]:
            while j < length-1  and arr[j] < arr[j+1]:
                j += 1
            profit += (arr[j] - arr[i])
            i = j

    return profit



if __name__ == "__main__":
    arr_list = [
        [],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [0, 1],
        [1, 0]
    ]
    func_list =[maxProfit_1,maxProfit_2, maxProfit_non_valleypeak ]
    print(maxProfit_non_valleypeak([1, 2, 3, 4, 5]))
    # List comprehension
    result_list = [list(map(func, arr_list)) for func in func_list]
    print (result_list)


