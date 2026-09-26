class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numRows = len(board)
        rowsNumSet = [set() for _ in range(numRows)]
        boxsNumSet = [set() for _ in range(numRows)]

        for rowIdx in range(numRows):
            row = board[rowIdx]
            rowNumSet = set()

            for colIdx in range(len(row)):
                num = row[colIdx]

                if num == '.':
                    continue
                
                print(f"num is {num}")

                if num in rowNumSet:
                    print('here0')
                    print(str(rowNumSet))
                    return False
                else:
                    if num in rowsNumSet[colIdx]:
                        print('here1')
                        print(str(rowsNumSet[colIdx]))
                        return False
                    
                    boxIdx = rowIdx // 3 * 3 + colIdx // 3
                    

                    if num in boxsNumSet[boxIdx]:
                        print('here3')
                        print(boxIdx)
                        print(str(boxsNumSet[boxIdx]))
                        return False
                    
                    rowNumSet.add(num)
                    rowsNumSet[colIdx].add(num)
                    boxsNumSet[boxIdx].add(num)

        print(str(rowsNumSet))
        print(str(boxsNumSet))
        return True


                    





        