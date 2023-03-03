# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        num = abs(x)
        while num > 0:
            last_digit = num % 10
            result = result * 10 + last_digit
            num //= 10
        if x < 0:
            result *= -1
        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
