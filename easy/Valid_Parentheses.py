#https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(': ')',
                   '[': ']',
                   '{': '}',
                   }
        stack = []
        for bracket in s:
            if bracket in hashmap:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if bracket != hashmap[stack.pop()]:
                    return False

        return len(stack) == 0


class _Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"))
