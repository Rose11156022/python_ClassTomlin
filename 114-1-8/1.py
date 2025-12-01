s = input()

o_win = 0
x_win = 0

if s[0] == s[1] == s[2] == 'O':
    o_win += 1
if s[3] == s[4] == s[5] == 'O':
    o_win += 1
if s[6] == s[7] == s[8] == 'O':
    o_win += 1

if s[0] == s[3] == s[6] == 'O':
    o_win += 1
if s[1] == s[4] == s[7] == 'O':
    o_win += 1
if s[2] == s[5] == s[8] == 'O':
    o_win += 1

if s[0] == s[4] == s[8] == 'O':
    o_win += 1
if s[2] == s[4] == s[6] == 'O':
    o_win += 1

if s[0] == s[1] == s[2] == 'X':
    x_win += 1
if s[3] == s[4] == s[5] == 'X':
    x_win += 1
if s[6] == s[7] == s[8] == 'X':
    x_win += 1

if s[0] == s[3] == s[6] == 'X':
    x_win += 1
if s[1] == s[4] == s[7] == 'X':
    x_win += 1
if s[2] == s[5] == s[8] == 'X':
    x_win += 1

if s[0] == s[4] == s[8] == 'X':
    x_win += 1
if s[2] == s[4] == s[6] == 'X':
    x_win += 1

if o_win > x_win:
    print(1)
elif x_win > o_win:
    print(2)
else:
    print(3)

