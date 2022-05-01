# 아직 풀어보는 중

import math

input_num = int(input())
k = math.log2(input_num/3)
start_point = input_num

def star(k, start_point) : 
  if k == 0 : 
    star_lst = [[" "," ","*"," "," "], 
                [" ","*"," ","*"," "],
                ["*","*","*","*","*"]] 
    for i in range(len(star_lst)) : 
      print("".join(star_lst[i]))                
    # print(" "*start_point + '*')
    # print(" "*(start_point-1) + '*' + " " + "*")
    # print(" "*(start_point-2) + '*'*5)
    return 0  
  else : 
    return star(k-1, start_point+5)
    
    
# star(k, start_point = 0) + 
star(k, start_point)

