class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right <= len(prices) - 1:
            #this should mean we have no profit.
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                curr_profit = prices[right] - prices[left]
                profit = max(curr_profit, profit)
                right += 1

        return profit


