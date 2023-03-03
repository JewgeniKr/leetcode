# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters
# and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        j = len(s) - 1
        i = 0
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome('0P'))