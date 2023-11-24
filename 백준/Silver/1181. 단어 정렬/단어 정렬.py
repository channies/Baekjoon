n = int(input())

arr_p = set()
for i in range(n):
    word = input()
    word_len = len(word)
    arr_p.add((word, word_len))

arr = list(arr_p)
arr.sort(key=lambda x : (x[1],x[0]))

for k in arr:
    print(k[0])
    