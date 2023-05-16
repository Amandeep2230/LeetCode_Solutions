class Solution:
    def maxArea(self, height: List[int]) -> int:
        #first: initialize pointers to beginning and end of height, ans as 0
        #second: loop throug until l<r, calc area between the two pointers and assign ans as max of area
        #thrid: increment left by 1 if its smaller than r, decrement r by 1 if its smaller than l and do either if they are equal
        #fourth: return ans after the loop
        l,r = 0, len(height)-1
        ans=0

        while(l<r):
            area=(r-l) * min(height[l],height[r])
            ans=max(ans,area)
            if (height[l]<height[r] and l<r):
                l+=1
            elif (height[l]>height[r] and l<r):
                r-=1
            else:
                l+=1
        return ans