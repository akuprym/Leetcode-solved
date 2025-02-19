'''''''''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''''''''

# 1
class Solution:
    def firstUniqChar (self, s: str) ->
        count = Counter (s)
        for i, m in enumerate(s) :
            if count [m] == 1:
                return i
        return -1

# 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for n in range(len(s)):
            if count[s[n]] == 1:
                return n
        return -1

