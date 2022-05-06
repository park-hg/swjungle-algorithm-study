# 159 ms 14.1 MB
# https://leetcode.com/problems/longest-substring-without-repeating-characters

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        substring = deque()
        max_len = 0

        for c in s:

            if c in substring:
                while substring:
                    cur = substring.popleft()
                    if cur == c:
                      break

            if c not in substring:
                substring.append(c)
                max_len = max(max_len, len(substring))

        return max_len
