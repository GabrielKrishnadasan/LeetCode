#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0

        f = 0
        letSet = set()

        for i in range(len(s)):
            if s[i] not in letSet:
                letSet.add(s[i])
            else:
                while s[f] != s[i]:
                    letSet.remove(s[f])
                    f += 1
                f += 1

            ret = max(ret, i - f + 1)