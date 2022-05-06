class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ans = 1
        for i in range(len(s)-1):
            substring = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                else:
                    break
                ans = max(ans, len(substring))
        return ans