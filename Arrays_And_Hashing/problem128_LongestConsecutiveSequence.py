class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first:make a set of nums and declare l as 0
        #second: loop through nums, see if 'i' is the first elemet of sequence
        #third: if it is, initialize length as 0, keep incrementing it by 1 until the next element is in the set
        #fouth: set the max of existing l and length as l, return l
        buffer=set(nums)
        l=0
        for i in nums:
            if (i-1) not in buffer:
                length=0
                while (i+length) in buffer:
                    length+=1
                l=max(l, length)
        return l