# https://leetcode.com/problems/length-of-last-word/

# Given a string s consisting of words and spaces, return the length of the
# last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

# my solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        result = 0
        while s[i] == ' ':
        # while s[i].isalpha() perhabs will be more fast
            i -= 1
        while s[i] != ' ' and i > -1:
            result += 1
            i -= 1
        return result

# with add memory
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = Solution()
if __name__ == '__main__':
    print(s.lengthOfLastWord('a'))
