class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first: initialize l,r as 1 and max vlaue of piles
        #second: perform binary search
        #third: if mid value less than or equal to h, set k as min of curent and mid value, and r as mid decremented by 1
        #fourth: else set l as mid incremented by 1
        l,r = 1, max(piles)
        k=r

        while (l<=r):
            mid = (l+r)//2
            count=0
            for i in piles:
                count += math.ceil(i/mid)
            if count<=h:
                k = min(k, mid)
                r = mid-1
            else:
                l = mid+1
        return k