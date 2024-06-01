import random

def read_file(length_word):
    with open('dictionary.txt', 'r') as file:
        word = [word.strip() for word in file.read().split() if len(word) == length_word]
        if not word:
            return None
        
        return random.choice(word)

def get_length():
    while True:
        try:
            length = int(input('How many length of word do you want to play? '))
            if length <= 2 or length >= 30:
                print('Invalid! The length of the word must be at least 3 and less than 30: ')
            else:
                return length
        except ValueError:
            print('Invalid! Re-enter the length of the word: ')

def get_letter(already_guessed):
    while True:
        letter = input('Which letter do you want to guess? ')
        if letter.upper():
            letter = letter.lower()
        
        if 'a' <= letter <= 'z' and len(letter) == 1:
            if letter not in already_guessed:
                return letter 
            else:
                print('You have already guessed that letter')
            
        else: 
            print('Invalid letter! Please try again: ')


def get_count():
    while True:
        try:
            count = int(input('How many times do you want to guess? '))
            if count > 0:
                return count
            else:
                print('Please enter a positive number: ')
        except ValueError:
            print('Invalid! Please re-enter the valid number: ')
            

def hangman_game():
    length = get_length()
    word = read_file(length)

    guessed_letter = []
    already_guessed = set()
    count = get_count()
    for i in range(len(word)):
        guessed_letter.append('-')
        print('-', end=' ')
    print()

    while count > 0 and '-' in guessed_letter:
        letter = get_letter(already_guessed)
        already_guessed.add(letter)
        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:        
                    guessed_letter[i] = letter
        else:
            count -= 1
            print("The letter '{}' is not in the word".format(letter))
            print('You have {} left to guess'.format(count))
        
        print('You have guessed: ', ' '.join(already_guessed))
        print('The current word is: ', ' '.join(guessed_letter))

    if '-' not in guessed_letter:
        print('Congratulation! The word is: {}'.format(word))
    else:
        print('You lost! The word is: {}'.format(word))


def main():
    hangman_game()
    while True:
        userInput = input('Do you want to continue the game?(y/n): ')
        if userInput == 'y' or userInput == 'Y':
            hangman_game()
        elif userInput == 'n' or userInput == 'N':
            break
        else:
            print("Invalid! You must enter 'y' or 'n'")


if __name__ == '__main__':
    main()
