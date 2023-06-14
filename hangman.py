from spanishWords import word_list
import random
import os

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("JUGUEMOS AL AHORCADO!!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("INGRESE UNA LETRA O PALABRA: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                os.system('cls')
                print("YA USASTE LA LETRA '", guess, "'")
            elif guess not in word:
                tries -= 1
                os.system('cls')
                print("'", guess, "' INCORRECTO, PIERDES 1 VIDA, TE QUEDAN "+str(tries)+" VIDAS")
                print("")
                guessed_letters.append(guess)
            else:
                os.system('cls')
                print("BIEN, '", guess, "' ESTA EN LA PALABRA")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                os.system('cls')
                print("ADIVINASTE LA PALABRA '", guess, "'")
            elif guess != word:
                os.system('cls')
                print("'",guess, "' NO ES LA PALABRA")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            os.system('cls')
            print("INGRESE UNA LETRA O PALABRA")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        os.system('cls')
        print("¡Felicidades, adivinaste la palabra! ¡Tú ganas!")
    else:
        print("PERDISTE, LA PALABRA ERA '" + word +"'")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                 -----
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                 -----
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                 -----
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                 -----
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 -----
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                 -----
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("QUIERES JUGAR DE NUEVO? (Y/N) ").upper() == "Y":
        os.system('cls')
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()