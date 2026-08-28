# history_quiz_portfolio.py
import pyfiglet
import colorama
from colorama import Fore
import csv
import random

colorama.init(autoreset=True)

# ================== QUESTIONS ==================
type Options = list[str]
type Question = dict[str, str | Options]
type Guess = list[str]

questions = [
    {"question": "In which year did World War II begin?", "options": ["1914", "1945", "1939", "1918"], "answer": "C"},
    {"question": "Who wrote the 95 Theses?", "options": ["Saint Augustus", "Martin Luther", "Voltaire", "John Calvin"], "answer": "B"},
    {"question": "On what island was Napoleon born?", "options": ["Corsica", "St Helena", "Sardinia", "Elba"], "answer": "A"},
    {"question": "In which country was the Battle of Hastings in 1066 fought?", "options": ["France", "England", "Germany", "Spain"], "answer": "B"},
    {"question": "Which woman discovered radium and polonium?", "options": ["Rosalind Franklin", "Ada Lovelace", "Maria Skłodowska-Curie", "Grace Hopper"], "answer": "C"},
    {"question": "When did the Berlin Wall fall?", "options": ["1989", "2000", "1961", "1991"], "answer": "A"},
    {"question": "What was Michelangelo's last name?", "options": ["Brunelleschi", "Buonarroti", "Botticelli", "Bellotto"], "answer": "B"},
    {"question": "In which year did Albert Einstein get the Nobel Prize?", "options": ["1955", "1916", "1905", "1921"], "answer": "D"},
    {"question": "Who was the first person in the world to land on the moon?", "options": ["Yury Gagarin", "Neil Armstrong", "Valentina Tereshkova", "Alan Shepard"], "answer": "B"},
    {"question": "What year did the French Revolution start?", "options": ["1799", "1917", "1815", "1789"], "answer": "D"}
]

# ================== FUNCTIONS ==================

def play_quiz(questions_list: list[Question]) -> tuple[Guess, int]:
    """
    Plays the quiz, asks each question, checks answers, and returns the guesses and score.
    
    Input Params:
        questions_list (list[Question]) : list of all the available quiz questions.

    Output:
        guesses, score : guesses are the total guessed answers, score is the player's total score
    """
    random.shuffle(questions_list)  # Randomize question order
    guesses = [] # list containing all the answers provided by the user
    score = 0 # current total score

    # For each question
    for i, q in enumerate(questions_list, start=1):
        # Display the question
        print(f"\nQuestion {i}: {q['question']}")

        # Create a dictionary with letters as its keys
        option_map = dict(zip(['A', 'B', 'C', 'D'], q['options']))

        # Display all the options together with their keys
        for key, val in option_map.items():
            print(f"{key}: {val}")

        # Ask the user to choose an option
        guess = input("Enter A, B, C or D (or 0 to quit): ").upper()
        
        # Input control: check for validity of the guess
        while guess not in 'ABCD0':
            guess = input("Invalid! Enter A, B, C or D: ").upper()

        if guess == '0':
            break

        guesses.append(guess)

        if guess == q['answer']:
            score += 1
            print(Fore.GREEN + "Correct!")
        else:
            print(Fore.RED + f"Incorrect! Correct answer was {q['answer']}")

    return guesses, score


def show_results(questions_list: list[Question], guesses: Guess, score: int):
    """
    Displays the final results, percentage score, ASCII art based on performance,
    and saves the score to a CSV file.

    Input Params:
        questions_list (list[Question]) : list of all the quiz questions
        guesses (Guess) : list of guessed answers for the player
        score (int) : current total score for the player
    """
    total_questions = len(questions_list)
    percent = round((score / total_questions) * 100)
    print("\n" + "="*40)
    print(f"You answered {score} out of {total_questions} correctly ({percent}%)")

    if percent == 100:
        print(Fore.CYAN + pyfiglet.figlet_format("Excellent!", font="slant"))
    elif percent >= 80:
        print(Fore.CYAN + pyfiglet.figlet_format("Very Good!", font="slant"))
    elif percent >= 60:
        print(Fore.CYAN + pyfiglet.figlet_format("Not Bad!", font="slant"))
    else:
        print(Fore.CYAN + pyfiglet.figlet_format("Keep Trying!", font="slant"))

    print("\nCorrect answers:", " ".join([q['answer'] for q in questions_list]))
    print("Your guesses:   ", " ".join(guesses))

    # Save results to CSV
    with open("quiz_results.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([score, total_questions, percent])
    print(Fore.CYAN + "\nYour result has been saved to quiz_results.csv")

# ================== MAIN ==================
if __name__ == '__main__':
    print(Fore.CYAN + pyfiglet.figlet_format("HISTORY QUIZ", font="standard"))
    print("Welcome! The quiz has 10 questions. Press 0 to quit anytime.")
    guesses, score = play_quiz(questions)
    show_results(questions, guesses, score)
