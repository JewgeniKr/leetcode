# https://leetcode.com/problems/fizz-buzz/description/

"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""


class Solution:
    def fizz_buzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result

    # The mod(%) operation is pretty slower than addition(+) operation,
    # and if you give a solution without using the mod operator,
    # even such easy question may still impressing interviewer
    # because you know much more a little bit.

    def _fizz_buzz(self, n: int) -> list[str]:
        result = []
        base3 = 3
        base5 = 5
        base15 = 3 * 5

        for i in range(1, n + 1):
            if i == base15:
                result.append('FizzBuzz')
                base3 += 3
                base5 += 5
                base15 += 15
            elif i == base3:
                result.append('Fizz')
                base3 += 3
            elif i == base5:
                result.append('Buzz')
                base5 += 5
            else:
                result.append(str(i))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s._fizz_buzz(15))
