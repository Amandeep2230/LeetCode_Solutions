class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first: initialize ans and sort the input list
        #second: loop through nums, continue if i is not the first element and a is one element before i
        #third: set pointers l and r as one more than i and last element of the list
        #fourth: check if target is less than 0, more than 0 or equal to 0
        #fifth: perform operations based on the result and result the triplet if equal to 0
        #sixth: increment l by 1 and keep incrementing until its not the same as last element 
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while (l<r):
                target = a+nums[l]+nums[r]
                if (target>0):
                    r-=1
                elif (target<0):
                    l+=1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans