class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first: perform binary search to find correct row
        #second: perform binary search on that row to get the right element
        rows, cols = len(matrix), len(matrix[0])

        t, b = 0, rows-1

        while (t<=b):
            m = (t+b)//2
            if target>matrix[m][-1]:
                t=m+1
            elif target<matrix[m][0]:
                b=m-1
            else:
                break
        
        if not (t<=b):
            return False
        m = (t+b)//2
        l,r = 0, cols-1
        while (l<=r):
            mid = (l+r)//2
            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid-1
            else:
                return True
        return False