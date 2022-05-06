# 8번째 문제 0506 https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s):
        substring = deque()
        max_length = 0
        for ss in s:
            if ss in substring:
                pop = substring.popleft()
                while substring and pop != ss:
                    pop = substring.popleft()
            substring.append(ss)
            max_length = max(max_length, len(substring))
        return max_length

sol = Solution()
sol.lengthOfLongestSubstring("abcabcbb")
sol.lengthOfLongestSubstring("bbbbb")
sol.lengthOfLongestSubstring("pwwkew")
sol.lengthOfLongestSubstring("aab")