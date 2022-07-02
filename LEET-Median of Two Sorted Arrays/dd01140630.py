nums1 = [-1,0,0,0,0,0,1]
nums2 = [0,0,0,0,0]

def sol(nums1, nums2):
    new = nums1 +nums2
    new = list(set(new))
    length = len(new)
    if length % 2 ==0:    
        return (new[length//2]+new[length//2 -1])/2
    
    else :
        return new[length//2]

print(sol(nums1,nums2))