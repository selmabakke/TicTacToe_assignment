import tkinter as tk
from tkinter import messagebox

# Global variables to keep track of the game state
current_player = "X"
game_board = ["", "", "", "", "", "", "", "", ""]

# Function to handle button clicks
def on_click(button, index):
    global current_player

    # If the button is already clicked, ignore
    if game_board[index] != "":
        return

    # Mark the clicked button and update the game board
    button.config(text=current_player, state="disabled")
    game_board[index] = current_player

    # Check if the current player has won
    if check_winner():
        for btn in buttons:
            btn.config(state="disabled")  # Disable all buttons when the game ends
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        return

    # Check if the game is a draw
    if all(game_board):
        messagebox.showinfo("Game Over", "It's a draw!")
        return

    # Switch players
    current_player = "O" if current_player == "X" else "X"

# Function to check if there's a winner
def check_winner():
    # Define all possible winning combinations
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for combo in winning_combinations:
        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]] != "":
            # Highlight the winning combination
            for idx in combo:
                buttons[idx].config(bg="lightgreen")
            return True
    return False

# Function to reset the game
def reset_game():
    global current_player, game_board
    current_player = "X"
    game_board = ["", "", "", "", "", "", "", "", ""]
    for button in buttons:
        button.config(text="", state="normal", bg="SystemButtonFace")  # Reset button text and color

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the 3x3 grid
buttons = []
for i in range(9):
    button = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: on_click(buttons[i], i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Add a reset button
reset_button = tk.Button(window, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

# Start the GUI event loop
window.mainloop()
