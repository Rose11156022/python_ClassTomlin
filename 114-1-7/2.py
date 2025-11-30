import sys

def game(s: str) -> int:
    # 將輸入字串分成 3x3 棋盤
    board = [
        [s[0], s[1], s[2]],
        [s[3], s[4], s[5]],
        [s[6], s[7], s[8]]
    ]
    
    def count_wins(player):
        wins = 0
        
        # 檢查橫線
        for row in board:
            if all(cell == player for cell in row):
                wins += 1
        
        # 檢查豎線
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                wins += 1
        
        # 檢查斜線（左上到右下）
        if all(board[i][i] == player for i in range(3)):
            wins += 1
        
        # 檢查斜線（右上到左下）
        if all(board[i][2-i] == player for i in range(3)):
            wins += 1
        
        return wins
    
    o_wins = count_wins('O')
    x_wins = count_wins('X')
    
    if o_wins > x_wins:
        return 1
    elif x_wins > o_wins:
        return 2
    else:
        return 3

if __name__ == "__main__":
    # Read all input from stdin
    input_data = sys.stdin.read().strip()
    if input_data:
        print(game(input_data))
