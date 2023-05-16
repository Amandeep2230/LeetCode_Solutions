class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first: intialize a hashmap and an empty list of list with length of elemts in nums
        #second: populate the hashmap with count of each element in nums
        #third: traverse through the hashmap, populate the list with count as index and the nums having that count as values
        #fourth: Traverse the list in reverse, traverse the sub-list and append in ans until the length matches 'k'
        buffer = {}
        res = [[] for i in range(len(nums)+1)]

        for x in nums:
            buffer[x] = 1 + buffer.get(x, 0)
        for x,c in buffer.items():
            res[c].append(x)
        ans = []
        for i in range(len(res)-1, 0, -1):
            for n in res[i]:
                ans.append(n)
                if len(ans)==k:
                    return ans