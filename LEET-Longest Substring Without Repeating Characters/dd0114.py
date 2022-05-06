from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        save = deque([])
        ans =0
        for i in s:
            if i in save:
                idx = save.index(i)
                for j in range(idx+1):
                    save.popleft()
                 
                save.append(i)

            else:
                save.append(i)
                ans = max(ans,len(save))
        
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))