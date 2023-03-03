# https://leetcode.com/problems/shuffle-the-array

# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i+n])
        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.shuffle([2,5,1,3,4,7], 3))