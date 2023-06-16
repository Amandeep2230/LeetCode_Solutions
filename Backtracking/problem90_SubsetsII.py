class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums):
                ans.append(subset[::])   #create copy of subset
                return
            
            #all subsets include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            #all subsets don't include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return ans