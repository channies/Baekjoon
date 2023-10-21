n = int(input())
dictionary = {}

for _ in range(n):
    title = input()
    if title in dictionary:
        dictionary[title] += 1
    else:
        dictionary[title] = 1

ans = []
max_value = max(dictionary.values())
for key, value in dictionary.items():
    if value == max_value:
        ans.append(key)

ans.sort()
print(ans[0])