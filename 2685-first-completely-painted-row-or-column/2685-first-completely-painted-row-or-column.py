class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        element_dict = dict()
        for i in range(m):
            for j in range(n):
                element_dict[mat[i][j]] = [i, j]
        
        row_dict = dict()
        column_dict = dict()

        for k in range(len(arr)):
            i, j = element_dict[arr[k]]
            row_dict[i] = 1 + row_dict.get(i, 0)
            column_dict[j] = 1 + column_dict.get(j, 0)

            if row_dict[i] == n or column_dict[j] == m:
                return k
        
        