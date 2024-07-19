class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColumnZero = False

        # Step 1: Determine if the first row or first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                firstColumnZero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
                break

        # Step 2: Use the first row and column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Zero out cells based on the markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out the first row and column if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        if firstColumnZero:
            for i in range(m):
                matrix[i][0] = 0
