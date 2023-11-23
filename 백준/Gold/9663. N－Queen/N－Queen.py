n = int(input())
arr = [0] * n
ans = 0

def promising(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x-i):
            return False
    return True

def nqueens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            arr[x] = i
            if promising(x):
                nqueens(x+1)
                
nqueens(0)
print(ans)