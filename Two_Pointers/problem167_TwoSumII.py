class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #first: declare two pointers pointing at first and last element of the list
        #second: if sum of elements at l and r is less than target, move l ahead by 1 else move r back by 1
        #third: if its equal to target then return by adding 1 to each l and r
        l,r = 0, len(numbers)-1
        while (l<r):
            if (numbers[l]+numbers[r]>target):
                r-=1
            elif (numbers[l]+numbers[r]<target):
                l+=1
            else:
                return(l+1, r+1)
        return
            