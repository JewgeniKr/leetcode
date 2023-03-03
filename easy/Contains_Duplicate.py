# https://leetcode.com/problems/contains-duplicate/solutions/?orderBy=newest_to_oldest

# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.

# my solution with a Set. It may be done with a hashmap.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))