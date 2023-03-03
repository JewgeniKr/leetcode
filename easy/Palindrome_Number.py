# https://leetcode.com/problems/palindrome-number

# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# ariphmetics
class Solution_:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        revers_num = 0
        while x != 0:
            revers_num = (revers_num * 10) + (x % 10)  # last num to forvard
            x = int(x / 10)  # del last num
        return temp == revers_num


if __name__ == '__main__':
    s = Solution_()
    print(s.isPalindrome(123))
