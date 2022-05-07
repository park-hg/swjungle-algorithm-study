from collections import defaultdict

#답을 참고했습니다...
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict()
        start_idx = 0
        max_len = 0
        for idx, ch in enumerate(s) :
            if ch in dic and start_idx <= dic[ch] :
                start_idx = dic[ch] + 1
            else:
                max_len = max(max_len, idx - start_idx + 1)
            
            dic[ch] = idx
            
        return max_len

        # dic = {}
#         str_list = []
#         if len(s) == 0:
#             return 0
#         elif s == " ":
#             return 1
#         else: 
#             for ch in s :
#                 if len(str_list) == 0:
#                     str_list.append(ch)
#                     continue
                    
#                 if ch not in str_list :
#                     temp = str_list[-1] + ch
#                     str_list.append(ch)
#                     str_list.append(temp)
#                 else:
#                     str_list.append(ch)
#             str_list.sort(key = len)
#             return len(str_list[-1])        
                    

        # answer = 0
        # temp = 0
        # str1 = ""
        # str2 = ""
        # if s == " ":
        #     return 1
        # else:
        #     for ch in s :
        #         if ch not in dic :
        #             dic[ch] = 1
        #             temp += 1
        #             str1 += ch        
        #         else:
        #             answer = max(answer, temp)
        #             dic.clear()
        #             dic[ch] = 1
        #             temp = 1
                   
        #     if temp > answer :
        #         answer = temp
            
        #     return answer