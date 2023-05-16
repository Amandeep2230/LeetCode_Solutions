class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first: initialize ans with length as nums
        #second: initialize pre as 1, loop through nums, ans[i] as pre and update pre with product of nums[i]
        #third: initialize post as 1, loop through nums, ans[i] as product with post, update post with product of nums[i]
        ans = [1]*len(nums)
        pre=1
        for i in range(len(nums)):
            ans[i]=pre
            pre*=nums[i]
        post=1
        for i in range(len(nums)-1, -1, -1):
            ans[i]*=post
            post*=nums[i]
        return ans