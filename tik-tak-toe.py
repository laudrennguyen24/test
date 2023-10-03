import tkinter as tk
import random

# Create the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Create the game window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', width=20, height=10)
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Function to handle button clicks
def button_click(position):
    if board[position] == ' ':
        board[position] = 'X'
        buttons[position].config(text='X')
        if not check_game_over():
            ai_move()

# Check if any player has won or the board is full
def check_game_over():
    winner = None
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            winner = board[combination[0]]
            break

    if winner:
        display_message(f"Player {winner} wins!")
        return True

    if ' ' not in board:
        display_message("It's a tie!")
        return True

    return False

# AI's move
def ai_move():
    possible_moves = [i for i, mark in enumerate(board) if mark == ' ']
    move = random.choice(possible_moves)
    board[move] = 'O'
    buttons[move].config(text='O')

    if not check_game_over():
        display_message("Your turn")


# Display a message in the game window
def display_message(message):
    message_label.config(text=message)

# Reset the game board
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ')
    display_message("Your turn")

# Create a message label
message_label = tk.Label(window, text="Your turn", font=("Time New Romans", 14))
message_label.grid(row=3, columnspan=3)

# Create a reset button
reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=4, columnspan=3)

# Bind the button clicks to the button_click function
for i, button in enumerate(buttons):
    button.config(command=lambda pos=i: button_click(pos))

# Start the game
reset_game()

# Run the game loop
window.mainloop()
