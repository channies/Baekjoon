import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [0] * (n*4)
    
arr = [int(input()) for _ in range(n)]

def init(start, end, index):
    if start == end:
        tree[index] = arr[start-1]
        return
    mid = (start+end) // 2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)
    tree[index] = tree[index*2] + tree[index*2+1]
    
def find(start, end, index, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[index]
    mid = (start+end) // 2
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sub_sum

def update(start, end, index, update_index, update_data):
    if update_index < start or update_index > end:
        return
    tree[index] += update_data
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, index*2, update_index, update_data)
    update(mid+1, end, index*2+1, update_index, update_data)
    
init(1,n,1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        temp = c-arr[b-1]
        arr[b-1] = c
        update(1,n,1,b,temp)
    elif a == 2:
        print(find(1,n,1,b,c))