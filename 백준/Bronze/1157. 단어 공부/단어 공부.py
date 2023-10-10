s = input().upper()
word = list(set(s))
numbers = []

for a in word:
    num = s.count(a)
    numbers.append(num)
    
if numbers.count(max(numbers)) >= 2:
    print("?")
else:
    print(word[numbers.index(max(numbers))])