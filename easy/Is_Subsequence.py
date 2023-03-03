# https://leetcode.com/problems/is-subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is
# a subsequence of "abcde" while "aec" is not).

# my own solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for char in t:
            if counter >= len(s):
                break
            if s[counter] == char:
                counter += 1
        return len(s) == counter


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence('abc', 'ahbgdc'))
