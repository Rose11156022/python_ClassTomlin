s = input()

lines = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

o_win = 0
x_win = 0

for line in lines:
    if s[line[0]] == s[line[1]] == s[line[2]] == 'O':
        o_win += 1
    if s[line[0]] == s[line[1]] == s[line[2]] == 'X':
        x_win += 1

if o_win > x_win:
    print(1)
elif x_win > o_win:
    print(2)
else:
    print(3)

