import random

print("\nWelcome to Hangman!\n")

words = ["angola","nigeria","ghana"]

scret_word = random.choice(words)
display_word = [] 

for letter in scret_word:
  display_word += "_"

guess_left = 5
game_over = False

while not game_over :
  print(f"\nYou have {guess_left} guesses left\n")
  guess = input("Guess a letter ")[0].lower()
  
  for position in range(len(scret_word)):
  
    letter = scret_word[position]
    if guess == letter:
      display_word[position] = letter
      
  if guess not in scret_word:
    guess_left -= 1
    if guess_left == 0:
      print("\nYou loser\n")
      game_over = True 
  
  if "_" not in display_word:
    print("\nYou win\n")
    game_over =  True
  print(f"\n {display_word}\n")