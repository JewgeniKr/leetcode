# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string

# with use bin() and foundation 2 on int()
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
    q = 2
