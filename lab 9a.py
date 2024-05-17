#Xintong Zhong

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors', 'paper':'rock','scissors':'paper'}
p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

class RockPaperScissors:
    def __init__(self, num_players=1):
        self.choices = ['rock', 'paper', 'scissors']
        self.beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        self.num_players = num_players
        self.scores = {'Player1': 0, 'Player2': 0, 'Draws': 0}
    
    def get_player_choice(self, player_number):
        choice = input(f'Player {player_number} - Pick one of rock, paper or scissors: ')
        while choice not in self.choices:
            choice = input("Invalid choice. Please choose again from rock, paper, or scissors: ")
        return choice
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, p1, p2):
        if p1 == p2:
            return "Draw"
        elif self.beats[p1] == p2:
            return "Player1"
        else:
            return "Player2"
    
    def play_round(self):
        if self.num_players == 0:
            p1 = self.get_computer_choice()
            p2 = self.get_computer_choice()
        elif self.num_players == 1:
            p1 = self.get_player_choice(1)
            p2 = self.get_computer_choice()
        else:
            p1 = self.get_player_choice(1)
            p2 = self.get_player_choice(2)
        
        winner = self.determine_winner(p1, p2)
        if winner == "Draw":
            self.scores['Draws'] += 1
        elif winner == "Player1":
            self.scores['Player1'] += 1
        else:
            self.scores['Player2'] += 1
            
        print(f"Player 1 chose {p1}, Player 2 chose {p2}. Result: {winner} wins this round.")
    
    def play_game(self):
        num_rounds = int(input("How many rounds do you want to play? "))
        for _ in range(num_rounds):
            self.play_round()
        print("Game over! Final Scores:")
        for key, value in self.scores.items():
            print(f"{key}: {value}")
            
num_players = int(input("Enter the number of human players (0, 1, or 2): "))
game = RockPaperScissors(num_players)
game.play_game()