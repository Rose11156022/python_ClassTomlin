n = int(input().strip())
d = 0
s = 0

while n > 0:
    if n % 2 == 0:
        n = n // 2
        d += 1
    else:
        n = n - 1
        s += 1

result = 2 * d + s
print(result)
