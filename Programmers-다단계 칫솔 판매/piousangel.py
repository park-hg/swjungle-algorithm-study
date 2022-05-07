# from collections import defaultdict

# 칫솔 한 개를 판매하여 얻어지는 이익은 100 
# “-“ 꼭대기
# 센터한테

def solution(enroll, referral, seller, amount):
    n_len = len(enroll)

    answer = [0 for _ in range(n_len)]
    p_dic = {}
    
    for i in range(n_len):
        p_dic[enroll[i]] = i

    for i in range(len(seller)):

        total = amount[i] * 100        #칫솔 개수 * 100 
        seller_name = seller[i]
        answer[p_dic[seller_name]] += total

        while referral[p_dic[seller_name]] != "-" :

            answer[p_dic[seller_name]] -= total//10  #10때고

            sangsa_name = referral[p_dic[seller_name]]   #상사에게 10퍼줘
            seller_name = sangsa_name

            answer[p_dic[seller_name]] += total//10 

            total = total//10 # -10퍼
            
            if total == 0:
                break

        answer[p_dic[seller_name]] -= total//10  #꼭대기도 센터한테 돈
        
    return answer

    