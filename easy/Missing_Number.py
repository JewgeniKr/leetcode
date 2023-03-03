# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# sum of series natural numbers = (k * (k + 1)) / 2 or (k**2 + k) / 2

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return ((n**2 + n) // 2) - sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
