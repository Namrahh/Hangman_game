import random
from Hangman_art import logo, stages
from Hangman_words import word_list2

print("----------------------------------------")
print(logo)
print("----------------------------------------")

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Hangman!")
print("Try to guess the word in less than 6 attempts")

chosen_word = random.choice(word_list2)
# print(chosen_word)

display = [ ]

turns = 6

game_over = False

for _ in range(len(chosen_word)):
  display += "_"
print(display)

while not game_over:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)

  if "_" not in display:
    game_over = True
    print("You win!")

  if guess not in chosen_word:
    turns -= 1
    print(f"Ooops! Wrong guess {name} The hangman is loosing his life")
  if turns == 0:
    game_over = True
    print("You lose!")
    print("You let a kind man die")
    print(f"The chosen word was:  {chosen_word}")

  print(stages[turns]) 
