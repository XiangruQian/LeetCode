class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if len(prices) == 0:
            return 0
        max_after = prices[-1]
        for i in range(len(prices)):
            index = len(prices) - (i + 1)
            max_after = max(max_after, prices[index])
            result = max(result, max_after - prices[index])
        return result


a = Solution()
print(a.maxProfit([]))