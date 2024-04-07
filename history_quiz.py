# -- IMPORT SECTION --------------------------------
import pyfiglet
import colorama
from colorama import Fore
colorama.init(autoreset=True)
# -------------------------------------------------

# -- FUNCTION DEFINITIONS ---------------------------
def play(questions, options, answers):
    """
    plays the quiz one question after the other. Stops if the user inputs 0.
    """
    guesses = []
    question_number = 0
    score = 0
    for question in questions:
        print("--------------------------------------")
        print(question)
        for option in options[question_number]:
            print(option)

        guess = input("Enter A, B, C or D: ").upper()
        while guess not in 'ABCD0':
            guess = input(f"The choice MUST be within A, B, C or D while you have typed {guess}.\nPlease, enter A, B, C or D: ").upper()
        guesses.append(guess)
        if guess == "0":
            break
        elif guess == answers[question_number]:
            score += 1
            print(Fore.GREEN + "Correct!")
        elif guess not in ("A", "B", "C", "D".upper()):
            print(Fore.YELLOW + "Sorry I don't understand ")
        else:
            print(Fore.RED + "Incorrect")

        question_number += 1

    return guesses, score

def show_results(questions, answers, guesses, score):
    """
    Shows the results as well as the overall mark.
    """
    print("========================================")
    result = "\tR\tE\tS\tU\tL\tT\t"
    print(result.center(21, '='))
    print()
    print("\tYou got " + str(score) + " of " + str(len(questions)) + " correct")

    if score == 10:
        result = pyfiglet.figlet_format("Congratulations", font="slant")
        print(result)
    elif score >= 8 and score < 10:
        result = pyfiglet.figlet_format("Very well", font="slant")
        print(result)
    elif score >= 6 and score <= 7:
        result = pyfiglet.figlet_format("Not bad !", font="slant")
        print(result)
    elif score <= 5:
        result = pyfiglet.figlet_format("Not very well ...", font="slant")
        print(result)

    print("------------------------------------")
    print("correct \nanswers: ", end='')
    for answer in answers:
        print(answer, end=' ')
    print()
    print("your \nguesses: ", end='')
    for guess in guesses:
        print(guess, end=' ')
    print()

    print("-------------------------------------")
# ---------------------------------------------------

# --- VARIABLE DECLARATIONS ----------------------------
questions = ("In which year did World War II begin?: ",
             "Who wrote a document known as the 95 Theses?: ",
             "On what island was Napoleon born?: ",
             "In which country was the Battle of Hastings in 1066 fought?: ",
             "What woman discovered radium and polonium?: ",
             "When did the Berlin Wall fall?: ",
             "What was Michelangelo's last name?:  ",
             "In which year did Albert Einstein get the Nobel Prize?: ",
             "Who was the first person in the world to land on the moon?: ",
             "What year did the French Revolution start?: ")

options = (("A: 1914", "B: 1945", "C: 1939", "D: 1918"),
           ("A: Saint Augustus", "B: Martin Luther", "C: Voltaire", "D: John Calvin"),
           ("A: Corsica", "B: St Helena", "C: Sardinia", "D: Elba"),
           ("A: France", "B: England", "C: Germany", "D: Spain"),
           ("A: Rosalind Franklin", "B: Ada Lovelace", "C: Maria Sklodowska-Curie", "D: Grace Hopper"),
           ("A: 1989", "B: 2000", "C: 1961", "D: 1991"),
           ("A: Brunelleschi", "B: Buonarroti", "C: Botticelli", "D: Bellotto"),
           ("A: 1955", "B: 1916", "C: 1905", "D: 1921"),
           ("A: Yury Gagarin", "B: Neil Armstrong", "C: Valentina Tereshkova", "D: Alan Shepard"),
           ("A: 1799", "B: 1917", "C: 1815", "D: 1789"))

answers = ("C", "B", "A", "B", "C", "A", "B", "D", "B", "D")
score = 0
question_number = 0
guess = None
# --------------------------

# --- MAIN -----------------
# Welcome the user
print(f"The quiz consists of {len(questions)} questions, each with four possible answers of which only one is correct. Press 0 as an answer to quit the quiz.")

# Play the game one question after the other
guesses, score = play(questions = questions, options = options, answers = answers)

# When the quiz is over, show the results
show_results(questions = questions, answers = answers, guesses = guesses, score = score)