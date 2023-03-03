# https://leetcode.com/problems/reverse-string
# Write a function that reverses a string. The input string is given as
# an array of characters s.
#
# You must do this by modifying the input array in-place
# with O(1) extra memory.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h", "e", "l", "l", "o"]))
