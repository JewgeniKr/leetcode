# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

class Solution:
    def single_number(self, nums: list[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.setdefault(nums[i], 0) + 1
        for key, value in hash_map.items():
            if value == 1:
                return key

    # this works faster
    def _singleNumber(self, nums: list[int]) -> int:
        dist = {}
        for i in nums:
            if i in dist:
                del dist[i]
            else:
                dist[i] = i
        for j in dist:
            return j

    # bit operation
    def __singleNumber(self, nums: list[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.single_number([4, 1, 2, 1, 2]))


