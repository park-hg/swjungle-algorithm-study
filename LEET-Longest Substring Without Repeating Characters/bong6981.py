## https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s) -> int:
    start = 0
    end = 0
    ans = 0
    dic = {}
    while start <= end and end < len(s):
        if start == end:
            dic[s[end]] = end
            ans = max(ans, 1)
            end += 1
            continue
        print(start, s[start], end, s[end], ans, dic)
        if (s[end] in dic) and (dic[s[end]] >= start) and end != dic[s[end]]:
            start = dic[s[end]] + 1
            dic[s[end]] = end
            if start > end:
                end = start + 1
        else:
            print(start, end)
            ans = max(ans, end-start+1)
            dic[s[end]] = end
            end += 1
        print(start, end)
    return ans

            




        
