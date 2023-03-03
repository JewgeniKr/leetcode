# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


# my binary_search
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start != end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        return start


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,7], 22))