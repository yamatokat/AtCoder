S = str(input())
T = str(input())

num = 0
for s, t in zip(S, T):
    if s == t:
        num += 1
print(num)
