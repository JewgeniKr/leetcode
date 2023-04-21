# https://leetcode.com/problems/happy-number/

"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not."""

"""Во множестве memory накапливаем суммы квадратов числа. Суть заключается в 
том, что если сумма нам уже встречалась на одной из предыдущих 
итерации, значит цикл будет бесконечным и нужно вернуть False"""


class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()
        while n not in memory:
            memory.add(n)
            n = sum((int(c) ** 2 for c in str(n)))
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
