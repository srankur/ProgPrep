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



if __name__ == "__main__":
    list = [2,1,3]
    print(list, maxProfit_1(list))
    print("[1,2,3,4,5,]", maxProfit_1([1,2,3,4,5]))
    print("[5,4,3,2,1]", maxProfit_1([5,4,3,2,1]))
    print("[0,1]", maxProfit_1([0,1]))
    print("[1,0]", maxProfit_1([1,0]))


    print(list, maxProfit_2(list))
    print("[1,2,3,4,5,]", maxProfit_2([1,2,3,4,5]))
    print("[5,4,3,2,1]", maxProfit_2([5,4,3,2,1]))
    print("[0,1]", maxProfit_2([0,1]))
    print("[1,0]", maxProfit_2([1,0]))
