class MaxProfit():
    def __init__(self, prices):
        self.prices = prices
    
    def maxProfitOneTransaction(self):
        """
        Time:O(N^2)
        Space:O(1)
        
        Returns:
            [int]: max profit with 1 transaction
        """
        curMaxProfit = 0
        for i in range(0, len(self.prices)-1):
            for j in range(i+1, len(self.prices)):
                diff = self.prices[j] - self.prices[i]
                if(diff > curMaxProfit):
                    curMaxProfit = diff
        return curMaxProfit

if __name__ == "__main__":
    obj = MaxProfit([7,1,5,3,6,4])
    print(obj.maxProfitOneTransaction())
