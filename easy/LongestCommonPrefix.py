# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of
# strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word = min(strs, key=len)
        for i in range(len(shortest_word), 0, -1):
            for elem in strs:
                if elem[:i] != shortest_word[:i]:
                    break
            else:
                return elem[:i]
        return ''


class _Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first , last = strs[0], strs[-1]
        index = 0
        while index < len(first) and index <len(last):
            if first[index] != last[index]:
                break
            index +=1

        return first[:index]


class __Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # strs = ["flower","flow","flight"]
        short = min(strs, key=len) # short = "flow"
        for item in strs: # When item = "flight"
            while len(short) > 0:
                if item.startswith(short): # during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
                    break
                else:
                    short = short[:-1] # during loop 1 short = flo, during loop 2 short = fl
        return short





if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['flower', 'flow', 'flight']))