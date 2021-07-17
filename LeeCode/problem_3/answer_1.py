from typing import List

'''
    思想：从右上角开始查找，相当于一个二叉树。左子树中叶子节点都小于根节点，右子树中节点都大于根节点。
        当前节点大于目标值，搜索当前节点的左子树，也就是当前位置的左侧格子
        当前节点小于目标值，搜索当前节点的右子树，也就是当前位置的右侧格子
    细节：
        1、在矩阵中，row取值[0,matrix.__len__()-1] col取值[0,matrix[0].__len__()-1]
        
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = matrix[0].__len__() - 1
        while (row < matrix.__len__() and col >= 0):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row = row + 1
            elif target < matrix[row][col]:
                col = col - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix, target))

    matrix_1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]]
    target_1 = 20
    print(solution.searchMatrix(matrix_1, target_1))
