# https://leetcode.com/problems/two-sum/
"""Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order."""


# BruteForce
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# HashMap
# add elem as key and index as value, that find target-nums[i] in dict
# {3: 0, # index: value
#  0: 1,
#  0: 2,
#  3: 3
#  }

class Solution_:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            different = target - nums[i]
            if different in hashmap:
                return [i, hashmap[different]]
            hashmap[nums[i]] = i
        return []


# two pointers (only if array is ordered) [1, 2, 3, 4, 5, 6, 7, 8, 9]
class Solution__:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        first_pointer = 0
        second_pointer = len(nums) - 1
        while first_pointer != second_pointer:
            current_sum = nums[first_pointer] + nums[second_pointer]
            if current_sum == target:
                return [first_pointer, second_pointer]
            elif current_sum < target:
                first_pointer += 1
            else:
                second_pointer -= 1


if __name__ == '__main__':
    s = Solution__()
    print(s.twoSum([1, 2, 3, 4, 5, 6, 8], 11))
