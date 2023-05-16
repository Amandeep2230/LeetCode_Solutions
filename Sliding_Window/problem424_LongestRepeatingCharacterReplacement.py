class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #first: initialize count as an empty hashmap, l as 0 and ans as 0
        #second: loop through the string, increment the count of s[r] by 1 
        #third: loop if number of operations that needs to be performed exceeds k, increment the postition of l by 1 and decrement the count of l by 1 in the hashmap
        #fourth: assign ans as max of current ans and the sequence, finally return ans in the end
        count = {}
        l=0 
        ans=0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r-l+1)-max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans