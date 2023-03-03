# https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

# my solution with two pointers
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j -= 1
            else:
                i += 1
        return nums


# my solution with swith elements
    def _moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s._moveZeroes([0, 0, 1]))
    print(s._moveZeroes([0, 1, 0, 3, 12]))
    print(s._moveZeroes([0, 0, 0, 0, 0, 0, 1, 1, 1]))
