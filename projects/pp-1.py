import random

word_bank = ["apple", "mango", "grapes", "banana"]

word = random.choice(word_bank)   # ✅ FIXED HERE

guessedword = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedword))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedword[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedword:
        print('Congratulations!! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedword:
    print('You have run out of attempts! The word was: ' + word)