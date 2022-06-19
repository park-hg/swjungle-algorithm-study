def solution(files):
    sort_info = []
    for k in range(len(files)):
        f = files[k]
        info = []
        idx = 0
        for i in range(len(f)):
            if f[i].isdigit():
                idx = i
                break
        
        head = f[:idx].lower()
        info.append(head)
        
        num_idx = idx
        for i in range(idx, idx+5):
            num_idx = i
            if not f[i].isdigit() :
                num_idx = i-1
                break
            if i == (len(f) - 1):
                break

        info.append(int(f[idx:num_idx+1]))
        info.append(k)
        sort_info.append(info)
    
    sort_info.sort()
    answer = []
    for e1, e2, idx in sort_info:
        answer.append(files[idx])
    return answer

files =["O00321", "O49qcGPHuRLR5FEfoO00321"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))