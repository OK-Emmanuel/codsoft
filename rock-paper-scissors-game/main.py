import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.iconbitmap("./rock-paper.ico")
        self.user_score = 0
        self.comp_score = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # User choice buttons
        tk.Label(self.master, text="Choose one:", font=("Segoe UI", 12)).pack(pady=10)
        self.rock_button = tk.Button(self.master, text="Rock", font=("Segoe UI", 10), width=10, command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)
        self.paper_button = tk.Button(self.master, text="Paper", font=("Segoe UI", 10), width=10, command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)
        self.scissors_button = tk.Button(self.master, text="Scissors", font=("Segoe UI", 10), width=10, command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)
        
        # Result display
        self.result_label = tk.Label(self.master, font=("Segoe UI", 12), pady=20)
        self.result_label.pack()
        
        # Score display
        self.score_label = tk.Label(self.master, text=f"User: {self.user_score} | Computer: {self.comp_score}", font=("Segoe UI", 12))
        self.score_label.pack()
    
    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        
        result = self.determine_winner(user_choice, comp_choice)
        self.display_result(user_choice, comp_choice, result)
        self.update_score(result)
    
    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "Tie"
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            return "User wins"
        else:
            return "Computer wins"
    
    def display_result(self, user_choice, comp_choice, result):
        self.result_label.config(text=f"User chose {user_choice}. Computer chose {comp_choice}. {result}")
    
    # Update score
    def update_score(self, result):
        if result == "User wins":
            self.user_score += 1
        elif result == "Computer wins":
            self.comp_score += 1
        
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.comp_score}")

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
