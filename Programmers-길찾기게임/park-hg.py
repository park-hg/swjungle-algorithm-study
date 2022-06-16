def solution(nodeinfo):
    # 93점
    
    def get_root(idx_list):
        max_height = -1
        max_idx = 0
        for idx in idx_list:
            if nodeinfo[idx][-1] > max_height:
                max_idx = idx
                max_height = nodeinfo[idx][-1]
        return max_idx
    
    def get_lr(idx_list, root):
        left, right = [], []
        for i in idx_list:
            if nodeinfo[i][0] < nodeinfo[root][0]:
                left.append(i)
            elif nodeinfo[i][0] > nodeinfo[root][0]:
                right.append(i)
        
        return left, right
            
    idx_list = list(range(len(nodeinfo)))

    pre_list = []
    def pre_order(pre):
        if pre:
            root = get_root(pre)
            left, right = get_lr(pre, root)
            pre_list.append(root+1)
            pre_order(left)
            pre_order(right)

    post_list = []
    def post_order(post):
        if post:
            root = get_root(post)
            left, right = get_lr(post, root)
            post_order(left)
            post_order(right)
            post_list.append(root+1)
            
    pre_order(idx_list)
    post_order(idx_list)

    return [pre_list, post_list]