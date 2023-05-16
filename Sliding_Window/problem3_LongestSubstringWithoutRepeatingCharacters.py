class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #first: initialize the set as buffer, l as 0 and ans as 0
        #second: loop through the string, run a while loop until the s[r] exists in the set, remove the leftmost element and keep incrementing l by 1
        #third: add the rightmost element to the set
        #fourth: set ans as max of current ans and 'r-l+1' and finally return it
        buffer= set()
        l=0
        ans=0

        for r in range(len(s)):
            while (s[r] in buffer):
                buffer.remove(s[l])
                l+=1
            buffer.add(s[r])
            ans = max(ans, r-l+1)
        return ans