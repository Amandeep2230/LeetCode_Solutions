class Solution:
    def findMin(self, nums: List[int]) -> int:
        #first: initialize l,r and ans
        #second: if value at l is less than value at r, it is the min value and break the loop
        #third: find mid, if value at mid is greater than equal to value at l, set l as mid incremented by 1
        #fourth: else, set r as mid decremented by 1, return ans after the while loop
        l,r = 0, len(nums)-1
        ans=nums[0]

        while (l<=r):
            if nums[l]<nums[r]:
                ans=min(ans, nums[l])
                break
            mid = (l+r)//2
            ans = min(ans, nums[mid])
            if nums[mid]>=nums[l]:
                l = mid+1
            else:
                r = mid-1
        return ans