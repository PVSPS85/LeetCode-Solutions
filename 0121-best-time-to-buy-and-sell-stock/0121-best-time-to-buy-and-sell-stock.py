class Solution(object):
    def maxProfit(self, prices):
        min = prices[0] 
        max  = 0
        for i in prices:
           
            if i < min :
                min = i

            profit = i - min 


            if profit > max :
                max = profit

        return max         