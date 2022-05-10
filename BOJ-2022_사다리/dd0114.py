import math
x,y,c = map(float, input().split())

left,right = min(x,y)

while(abs(right-left)>1e-6):
    mid = (left+right)/2
    d= mid
    h1 = math.sqrt(x**2 - d**2)
    h2 = math.sqrt(y**2 - d**2)
    h = (h1*h2)/(h1+h2)
    if h > c:
        left = mid
    
    else:
        right = mid

print("%.3f"%round(mid,3))
