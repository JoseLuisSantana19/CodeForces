input = input().split()
n, m, a = int(input[0]), int(input[1]), int(input[2])
if n % a == 0:
    n = n / a
else:
    n = (n//a) + 1
if m % a == 0:
    m = m / a
else:
    m = (m//a) + 1
print('{:.0f}'.format(m*n))
