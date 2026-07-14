class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        prof = 0
        for i in range(0, l):
            buy = prices[i]
            for j in range(i, l):
                if j != i:
                    sell = prices[j]
                    prof = max(prof, sell - buy)
        return prof