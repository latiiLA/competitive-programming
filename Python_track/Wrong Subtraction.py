n, k = input().split()

i = 0

while i < int(k):
    if int(n[-1]) > 0:
        n = str((int(n) - 1))
    elif int(n[-1]) == 0:
        n = str(int(n) // 10)
    
    i += 1

print(int(n))
