#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1 , -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)

        return digits


class _Solution(object):
    def plusOne(self, digits):
        # Adjusting an array of digits into an integer
        digits_integer = int(''.join(map(str,digits)))
        digits_integer +=1
        # Adjusting back an integer into an array of digits after plus 1
        return [int(x) for x in str(digits_integer)]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 9, 9]))
