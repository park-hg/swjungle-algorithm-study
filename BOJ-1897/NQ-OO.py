
import sys
input = sys.stdin.readline

d, start_word = input().split()

dict_lst = [input().strip() for _ in range(int(d))]
dict_lst.sort(key=len)

able_str_lst = [start_word]
dict_lst.remove(start_word)

for single_str in dict_lst : 
  for str_idx in range(len(single_str)) :
    temp_str = single_str[:str_idx] + single_str[str_idx+1 :]
    if temp_str in able_str_lst : 
      able_str_lst.append(single_str)
      break

print(max(able_str_lst,key=len))
    
    
    
    





