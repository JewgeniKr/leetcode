# https://leetcode.com/problems/single-element-in-a-sorted-array/

# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# binary search
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                end = mid
            else:
                start = mid + 2
        return nums[start]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([2, 2, 3, 3, 4, 4, 8, 8, 9]))
