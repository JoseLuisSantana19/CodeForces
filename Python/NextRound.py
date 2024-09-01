n, k = map(int, input().split())
array = list(map(int, input().split()))
cont = 0
ind = 0
while ind < n:
    if array[ind] == 0:
        break
    else:
        if (ind < k) or (ind < n and array[ind] == array[ind - 1]):
            cont += 1
        else:
            break
    ind += 1
print(cont)
