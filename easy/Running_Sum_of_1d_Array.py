# https://leetcode.com/problems/running-sum-of-1d-array

"""
Given an array nums. We define a running sum of an array
as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        i = 1
        while i < len(nums):
            nums[i] += nums[i - 1]
            i += 1
        return nums

    # так как i увеличивается на каждой итерации можно заменить на
    def _runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == '__main__':
    print(Solution()._runningSum([1, 2, 3, 4]))
