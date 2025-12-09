import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
lives = 6

print(f"{hangman_art.logo}")

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Your word is: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************[{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in incorrect_letters:
        print("You've guessed that letter already! Try a different one")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Your word is: " + display)

    if guess not in chosen_word:
        lives -= 1
        incorrect_letters.append(guess)
        print(f"'{guess}' is not in this word, try again!")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\n"
                  f"the word was: {chosen_word}\n")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
