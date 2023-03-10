# https://leetcode.com/problems/pascals-triangle/

"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly
above it as shown:
"""


class Solution:
    def generate(self, numrows: int) -> list[list[int]]:
        result = [[1 for _ in range(i)] for i in range(1, numrows + 1)]
        if len(result) > 2:
            for i in range(2, len(result)):
                for j in range(1, i):
                    result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
