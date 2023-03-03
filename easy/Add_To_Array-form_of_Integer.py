# https://leetcode.com/problems/add-to-array-form-of-integer
# The array-form of an integer num is an array representing its digits in left
# to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return
# the array-form of the integer num + k.


# my brood force
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        num_from_list = 0
        mult = 1
        for number in num[::-1]:
            num_from_list += number * mult
            mult *= 10

        sum_number = num_from_list + k

        new_sum = []
        while sum_number > 0:
            new_sum.append(sum_number % 10)
            sum_number //= 10

        return new_sum[::-1]

# optimal solution
class Solution_:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        n = len(num)
        carry = 0
        i = n - 1
        while k > 0 or i >= 0 or carry > 0:
            sum = carry
            if k > 0:
                remainder = k % 10
                sum += remainder
                k //= 10
            if i >= 0:
                sum += num[i]
                i -= 1
            carry = sum // 10
            ans.insert(0, sum % 10)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm([1, 2, 0, 0], 34))
