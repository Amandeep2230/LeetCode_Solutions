class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first: loop through the strs and declare count based on the alphabets
        #second: for each char in the string, we fetch the ASCII value using ord to know the exact alphabet and have a count of that letter
        #third: add the key value pair of count and a list of the strings having the same count
        #fourth: display the values in the hashmap
        buffer=defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char)-ord('a')]+=1
            buffer[tuple(count)].append(i)
        return buffer.values()