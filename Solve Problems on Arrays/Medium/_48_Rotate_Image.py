def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        # Brute force method
        # Beats 19.55% of users with Python3
        rowL = []
        newMat = []
        for i in range(len(matrix)):
            rowL = []
            for j in range(len(matrix)-1, -1, -1):
                # matrix[row][col] = matrix[j][i]
                # print(matrix[j][i], end='')
                rowL.append(matrix[j][i])
            newMat.append(rowL)
        # matrix = newMat
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=newMat[i][j]
        # print(matrix)
        """

        # Beats 77.78% of users with Python3
        n = len(matrix)
    
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()
