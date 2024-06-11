def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        rowDic = {}
        colDic = {}
        for i in row:
            # print(i)
            if i in rowDic:
                rowDic[i] += 1
            else:
                rowDic[i] = 1
        # print(list(rowDic.keys()))
        row = list(rowDic.keys())
        print(row)
        for i in col:
            # print(i)
            if i in colDic:
                colDic[i] += 1
            else:
                colDic[i] = 1
        # print(list(colDic.keys()))
        col = list(colDic.keys())
        print(col)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
