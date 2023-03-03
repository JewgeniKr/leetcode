# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and
# false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of
# a different word or phrase, typically using all the original letters
# exactly once.

# my solution with two hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hash_s = {}
            hash_t = {}
            for i in range(len(s)):
                hash_s[s[i]] = hash_s.setdefault(s[i], 0) + 1
                hash_t[t[i]] = hash_t.setdefault(t[i], 0) + 1
        return hash_s == hash_t


if __name__ == '__main__':
    s = Solution()
    s.isAnagram("anagram", "nagaram")
