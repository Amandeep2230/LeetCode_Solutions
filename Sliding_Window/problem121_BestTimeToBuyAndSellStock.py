class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #first: initialize l, r as 0,1 and maxP as 0
        #second: loop until r is less than len of prices
        #third: if price of l is less than r, calc profit and assign it to maxP if its more than current maxP
        #fourth: else set l as r as its the lowest price seen so far, keep incrementing r by 1 and finally return maxP
        l,r = 0,1
        maxP=0
        while (r<len(prices)):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP