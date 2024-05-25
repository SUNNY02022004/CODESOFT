import math

# Define the game board
def print_board(board):
    for row in board:
        print(" " + " | ".join(row) + " ")
        print("---|---|---")
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    if winner == 'O':
        return 1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_turn = True

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'X':
                print("Human wins!")
            else:
                print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        if human_turn:
            move = None
            while move not in range(1, 10):
                move = input("Enter your move (1-9): ")
                if move.isdigit():
                    move = int(move)
                else:
                    move = None
            move = (move - 1) // 3, (move - 1) % 3
            if board[move[0]][move[1]] == ' ':
                board[move[0]][move[1]] = 'X'
                human_turn = False
            else:
                print("Invalid move! Try again.")
            
            # Print a separation gap
            print("\n" * 2)
        else:
            move = best_move(board)
            board[move[0]][move[1]] = 'O'
            human_turn = True

if __name__ == "__main__":
    play_game()
