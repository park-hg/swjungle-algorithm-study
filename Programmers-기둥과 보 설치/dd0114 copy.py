box = []
answer = []
end = 0

def check(x,y,a):
    global end
    flag = 0
    if a == 0:
        if y == end:
            return flag
        elif y == 0:
            flag = 1
        elif box[y-1][x][0]:
            flag = 1
        else :
            right = box[y][x][1]
            if x == 0 and right:
                flag = 1
            else :
                left = box[y][x-1][1]
                if left and right :
                    return flag
                elif left or right :
                    flag = 1

    else :
        if y == 0 or x == end:
            return flag
        elif box[y-1][x][0] or box[y-1][x+1][0]:
            flag =1 
        elif x == 0:
            return flag
        elif box[y][x-1][1] and box[y][x+1][1]:
            flag = 1
    
    return flag
    

def solution(n, build_frame):
    global end
    for i in range(n+1):
        new_box = [[False,False]for _ in range(n+1)]
        box.append(new_box)
    
    end = n

    for i in build_frame:
        x,y,a,b = i

        if b == 1 :
            if check(x,y,a) : 
                answer.append([x,y,a])
                box[y][x][a] = True

        else :
            box[y][x][a] = False
            if a == 0:
                if 0 < x :
                    if box[y+1][x-1][1] :
                        if not check(x-1,y+1,1):
                            box[y][x][a] = True
                            continue

                if box[y+1][x][0]:
                    if not check(x,y+1,0):
                        box[y][x][a] = True
                        continue
                    
                if box[y+1][x][1]:
                    if not check(x,y+1,1):
                        box[y][x][a] = True
                        continue

            else :
                if 0<x :
                    if box[y][x-1][1]:
                        if not check(x-1,y,1):
                            box[y][x][a] = True
                            continue
                if box[y][x][0]:
                    if not check(x,y,0):
                        box[y][x][a] = True
                        continue
                if box[y][x+1][1]:
                    if not check(x+1,y,1):
                        box[y][x][a] = True
                        continue
                if box[y][x+1][0]:
                    if not check(x+1,y,0):
                        box[y][x][a] = True
                        continue
                
            tmp = [x,y,a]
            answer.pop(answer.index(tmp))

    answer.sort()
    return answer


n = 100
# build_frame	= [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
build_frame = [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]

print(solution(n, build_frame))