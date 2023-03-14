# https://leetcode.com/problems/isomorphic-strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in map_st and map_st[c1] != c2) or
                    (c2 in map_ts and map_ts[c2] != c1)):
                return False
            map_st[c1] = c2
            map_ts[c2] = c1

        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("egg", "add"))
