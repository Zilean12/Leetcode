# Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        print("Maximum profit:", max_profit)
        return max_profit
        
sol = Solution()
prices = [7,1,5,3,6,4]
sol.maxProfit(prices)

        