class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        ans = 1
        substring = []
        for i in range(len(s)):
            if s[i] in substring:
                idx = substring.index(s[i])
                substring = substring[idx+1:]
            substring.append(s[i])
            ans = max(ans, len(substring))
        return ans