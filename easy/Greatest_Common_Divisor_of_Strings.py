# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Поиск наибольшего общего делителя - алгоритм Евклида
# в питоне есть функция math.gcd(a, b)

"""For two strings s and t, we say "t divides s" if and only if
s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such
that x divides both str1 and str2."""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ''
        gsd = self.recurs(len1, len2)
        return str2[:gsd]

    def evklid(self, num1, num2):
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1

    def recurs(self, a, b):
        if b == 0:
            return b
        else:
            self.recurs(b, a % b)


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings('ABCABCABCABCABCABCABC', 'ABCABCABC'))
