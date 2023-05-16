class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #first: initialize three dictionary sets for rows, cols and square of 9x9
        #second: loop through to get to the element such that it is representes as board[rows][cols]
        #third: continue the loop if element is empty
        #fourth: check if element already exists in any of the sets and return false if it does
        #fifth: add element to set if it doesn't exist in the set
        #sixth: return true if the loop completes
        setX=collections.defaultdict(set)
        setY=collections.defaultdict(set)
        set9=collections.defaultdict(set)

        for x in range(9):
            for y in range(9):
                if (board[x][y]=="."):
                    continue
                if (board[x][y] in setX[x] or board[x][y] in setY[y] or board[x][y] in set9[(x//3, y//3)]):
                    return False
                setX[x].add(board[x][y])
                setY[y].add(board[x][y])
                set9[(x//3, y//3)].add(board[x][y])
        return True