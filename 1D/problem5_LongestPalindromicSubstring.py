class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        count = 0

        for i in range(len(s)):
            #for odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>count:
                    ans = s[l:r+1]
                    count = r-l+1
                l-=1
                r+=1
            
            #for even length
            l,r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>count:
                    ans = s[l:r+1]
                    count = r-l+1
                l-=1
                r+=1
        
        return ans