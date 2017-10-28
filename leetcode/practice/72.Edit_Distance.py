import pprint


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix = []
        cols = len(word1) + 1
        rows = len(word2) + 1

        for row in range(rows):
            matrix.append([0] * cols)

        for initial_value in range(cols):
            matrix[0][initial_value] = initial_value

        for initial_value in range(rows):
            matrix[initial_value][0] = initial_value

        for col_index in range(1, cols):
            for row_index in range(1, rows):
                if word1[col_index - 1] == word2[row_index -1]:
                    matrix[row_index][col_index] = matrix[row_index-1][col_index-1]
                else:
                    matrix[row_index][col_index] = min(matrix[row_index-1][col_index-1],
                                                       min(matrix[row_index][col_index-1],
                                                           matrix[row_index-1][col_index])) + 1

        return matrix[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("ab", "bc"))
    str1 = "azced"
    str2 = "abcdef"
    print(s.minDistance(str1, str2))
    print(s.minDistance("b", "c"))
    print(s.minDistance("b", ""))
    print(s.minDistance("ab", "a"))

