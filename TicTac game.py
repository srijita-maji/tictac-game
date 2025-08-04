def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    # Check for draw
    if " " not in board:
        return "draw"
    
    return None

def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8:
                if board[move] == " ":
                    return move
                else:
                    print("That position is already taken!")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1 to 9 left to right, top to bottom")
    
    while True:
        print_board(board)
        move = get_player_move(current_player, board)
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
