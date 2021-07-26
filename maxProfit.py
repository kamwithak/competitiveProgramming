"""
MaxProfit Class!
Finds a maximum achievable profit
"""

import sys

class MaxProfit():
    def __init__(self, prices):
        self.prices = prices
        self.numberOfDays = len(prices)

    def maxProfitOneTransactionLinear(self):
        """
            Time: O(N)
            Space: O(1)
            
            Returns:
                [int]: max profit with 1 transaction
        """
        bestPriceToBuy, bestDayToBuy = sys.maxsize, 0
        bestPriceToSell, bestDayToSell = -sys.maxsize, 0
        numberOfBetterPricesForBuying = 1
        
        for day, price in enumerate(self.prices):

            if (price < bestPriceToBuy):
                bestDayToBuy = day
                bestPriceToBuy = price
                numberOfBetterPricesForBuying += 1
            elif (price > bestPriceToSell):
                bestDayToSell = day
                bestPriceToSell = price

            if (numberOfBetterPricesForBuying == self.numberOfDays):
                return 'Unprofittable'

        print(f"Bought on Day#{bestDayToBuy+1} and Sold on Day#{bestDayToSell+1}")

        return bestPriceToSell - bestPriceToBuy

    def maxProfitOneTransactionQuadratic(self):
        """
            Time: O(N^2)
            Space: O(1)
            
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
    obj = MaxProfit([10,9,8,7,6,5,4,6,7,8,9])
    print(obj.maxProfitOneTransactionLinear())
    # print(obj.maxProfitOneTransactionQuadratic())