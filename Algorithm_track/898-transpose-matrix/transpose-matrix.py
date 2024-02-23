class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_matrix = [ [0 for row in range(len(matrix))] for col in range(len(matrix[0]))]

        for i in range(len(matrix[0])):
            # print(i)
            for j in range(len(matrix)):
                result_matrix[i][j] += matrix[j][i]
            
        return result_matrix

        