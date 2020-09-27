class MaxProfit():
    def __init__(self, prices):
        self.prices = prices
    
    def maxProfitOneTransaction(self):
        prices = self.prices
        curMax = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if(diff > curMax):
                    curMax = diff
        return curMax

if __name__ == "__main__":
    obj = MaxProfit([7,6,4,3,1])
    print(obj.maxProfitOneTransaction())
