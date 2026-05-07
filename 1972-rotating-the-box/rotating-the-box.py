class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m,n=len(boxGrid),len(boxGrid[0])
        for row in range(m):
            newrow = []
            obstIndex = -1
            for col in range(n):
                if boxGrid[row][col] == "*":
                    newrow.append(boxGrid[row][col])
                    obstIndex = col
                elif boxGrid[row][col] == ".":
                    if obstIndex>=0:newrow = newrow[:obstIndex+1] + ["."] + newrow[obstIndex+1:]
                    else:newrow = ["."] + newrow
                else:
                    newrow.append(boxGrid[row][col])
            boxGrid[row] = newrow
        rotatedBoxGrid = []
        for col in range(n):
            newRow = []
            for row in range(m):
                newRow.append(boxGrid[row][col])
            newRow = newRow[::-1]
            rotatedBoxGrid.append(newRow)
        return  rotatedBoxGrid