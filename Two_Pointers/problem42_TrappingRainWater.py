class Solution:
    def trap(self, height: List[int]) -> int:
        #first: return 0 if height is empty
        #second: initialize l, r as 0 first and last element, maxL and maxR as height of current l and r, ans as 0
        #third: if maxL<maxR, increment l by 1, store maxL as max of current maxL and height[l] and increment ans to difference of maxL and height[l]
        #fourth: else, decrement r by 1, store maxR as max of current maxR and height[r] and increment ans to difference of maxR and height[r]
        #fifth: return ans
        if not height: return 0

        l,r = 0, len(height)-1
        maxL,maxR = height[l], height[r]
        ans=0

        while (l<r):
            if maxL<maxR:
                l+=1
                maxL=max(maxL, height[l])
                ans += maxL - height[l]
            else:
                r-=1
                maxR=max(maxR, height[r])
                ans+=maxR - height[r]
        return ans