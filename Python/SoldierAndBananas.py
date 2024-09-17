k, n, w = map(int, input().split())
totalValue = 0
for e in range(1, w+1):
    totalValue += e * k
if totalValue > n:
    print(totalValue - n)
else:
    print(0)
