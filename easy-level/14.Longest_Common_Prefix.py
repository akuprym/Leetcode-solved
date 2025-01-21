'''''''''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''''''''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        for i in strs:
            while not i.startswith(pref):
                pref = pref[:-1]
                if not pref:
                 return ""
        return pref
