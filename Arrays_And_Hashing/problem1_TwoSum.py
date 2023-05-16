class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first: get a difference of target and num, if its not in buffer then add the value,index pair to buffer
        #second: if the difference is in buffer then return the value of 'i' and value of differenc in buffer
        buffer = {}
        for i, num in enumerate(nums):
            total = target-num
            if (total in buffer):
                return [i, buffer[total]]
            buffer[num]=i
        return