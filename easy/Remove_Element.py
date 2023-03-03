#https://leetcode.com/problems/remove-element/
#Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The relative order of the elements may be changed.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))