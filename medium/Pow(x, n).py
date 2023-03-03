from flask import Flask
# https://leetcode.com/problems/powx-n/
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# It's not that wants to see the interviewer )
class Solution:
    def myPow(self, x: float, n: int) -> float:
        x ** n


# really solution
class Solution_:
    def myPow(self, x: float, n: int) -> float:
        # Deal with negative power:
        # a ** -n == 1 / a ** n
        if n < 0:
            x = 1 / x
            n = n * -1

        # Iterate:
        result = 1
        while n != 0:
            if n % 2 != 0:
                result = result * x
            x = x * x
            n = n // 2

        return result


if __name__ == '__main__':
    s = Solution_()
    print(s.myPow(2.00000, 10))
