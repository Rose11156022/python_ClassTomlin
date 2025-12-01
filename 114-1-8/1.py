import sys


def main() -> None:
	data = sys.stdin.read().strip()
	if not data:
		return
	# 擷取 O 和 X，並取前 9 個字元（題目保證長度為 9）
	s = ''.join(ch for ch in data if ch in ('O', 'X'))[:9]
	if len(s) < 9:
		# 若輸入不完整，直接補空格（不會形成三連線）
		s = s.ljust(9)

	# 建立 3x3 棋盤（row-major）
	board = [list(s[i * 3:(i + 1) * 3]) for i in range(3)]

	lines = []
	# 橫列
	for i in range(3):
		lines.append([board[i][j] for j in range(3)])
	# 直列
	for j in range(3):
		lines.append([board[i][j] for i in range(3)])
	# 兩條斜線
	lines.append([board[i][i] for i in range(3)])
	lines.append([board[i][2 - i] for i in range(3)])

	o_count = 0
	x_count = 0
	for line in lines:
		if all(c == 'O' for c in line):
			o_count += 1
		if all(c == 'X' for c in line):
			x_count += 1

	if o_count > x_count:
		print(1)
	elif x_count > o_count:
		print(2)
	else:
		print(3)


if __name__ == '__main__':
	main()

