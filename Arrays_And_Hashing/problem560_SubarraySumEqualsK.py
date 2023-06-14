class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        buffer = {
            0 : 1
        }

        for i in nums:
            curSum += i
            diff = curSum - k

            ans += buffer.get(diff, 0)
            buffer[curSum] = 1 + buffer.get(curSum, 0)
        
        return ans