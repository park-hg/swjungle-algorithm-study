def solution(n, k, cmd):
    answer = ''
    idx = k
    dic = {} 
    
    CD_list = ['C','Z']
    re_box = []
    for i in range(n) :
        dic[i] = 'O'
        
    for info in cmd :
        # print(re_box)
        # print(dic)
        if info in CD_list : 
            if info == CD_list[0] :   # 'C'
            
                # x 표시하면서 순서 기록해야
                dic[idx] = 'X'
                re_box.append(idx)
                cnt = 1
                
                while idx >= 0 :
                    if dic[idx-cnt] == 'O':
                        idx = idx + cnt
                        break
                    else:
                        cnt += 1
   
            else:   # 'Z' 리박스 맨뒤에거 복구
                # print("ZZZZZZZ")
                dic[re_box[-1]] = 'O'
                del re_box[-1]
        else:
            arrow, num = map(str, info.split())
            temp = int(num)
            cnt = 1
            if arrow == 'D' :
             
                while temp > 0 :
                    if dic[idx + cnt] == 'O' :
                        temp -= 1
                    cnt += 1
                idx += cnt-1
            
            else:  # 'U'
                while temp > 0 :
                    if dic[idx - cnt] == 'O' :
                        temp -= 1
                    cnt += 1
                idx -= cnt-1
    # print(dic)
    for key, value in dic.items():
        answer += value
    return answer