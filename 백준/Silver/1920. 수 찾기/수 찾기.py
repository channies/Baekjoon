import sys
input = sys.stdin.readline

n = int(input())
a_arr = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

for num in arr:
    if num in a_arr:
        print(1)
    else:
        print(0)
