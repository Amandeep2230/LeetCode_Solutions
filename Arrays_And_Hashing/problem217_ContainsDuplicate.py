class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #initialize a set as it can't have duplicate values
        #loop through nums, return true if value already exists else add the value to the set
        #if it loops through all the elements in nums, means no duplicate value
        
        buffer = set()
        for i in nums:
            if i in buffer:
                return True
            buffer.add(i)
        return False