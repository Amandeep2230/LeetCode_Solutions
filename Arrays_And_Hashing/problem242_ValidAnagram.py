class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first: pass the string s into buffer to have a list of all characters
        #second: traverse through t and check if that character exists in buffer, del if it exists 
        #third: if buffer is empty then its anagram else not an anagram
        buffer = []
        for i in s:
            buffer.append(i)
        for j in t:
            if (j in buffer):
                buffer.remove(j)
            else:
                return False
        if buffer:
            return False
        else:
            return True