s = input().strip()

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        if int(''.join(lst)) % 29 == 0:
            print(1)
            raise SystemExit
print(0)
