def maxProfit(self, prices: List[int]) -> int:
        """
        # Time Limit Exceeded O(n2)
        if not prices or len(prices) < 2:
            return 0  # No profit possible if there are less than 2 prices
    
        maxP = 0  # Initialize max profit as 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):  # Ensure j starts from i + 1
                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
        return maxP
        """
  # O(n)
    profit = 0 
        buy=prices[0]

        for i in range(1,len(prices)):
            if(prices[i]>buy):
                profit = max(profit,prices[i]-buy)
            else:
                buy=prices[i]
        return profit
