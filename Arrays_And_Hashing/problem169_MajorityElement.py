class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        buffer = {}
        ans, maxC = 0,0

        for i in nums:
                buffer[i] = 1 + buffer.get(i, 0)
                ans = i if buffer[i] > maxC else ans
                maxC = max(maxC, buffer[i])
        return ans