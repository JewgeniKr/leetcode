# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

"""
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # without string methods
    def _strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(0, haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('sadbutsad', 'arrr'))
