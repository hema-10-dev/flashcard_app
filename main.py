import html
from pathlib import Path
import json

path = Path('flashcards.json')

file_text = path.read_text()
contents = json.loads(file_text)

question_list = contents["results"]

pts = 0
for question in question_list:
    display_ques = question["question"]
    clean_question = html.unescape(display_ques)
    display_answer = question["correct_answer"]
    display_incorrect = question["incorrect_answers"]
    print(f"The question is:\n {clean_question}")
    print("\n The answers are")
    all_options = [display_answer]+display_incorrect
    for option in sorted(all_options):
        print(option)
    user_ans = input("Enter your answer:   ")
    if user_ans.lower() == display_answer.lower():
        pts += 100
        #print(f"You have scored {pts} points")
        print("Your answer is right")
    else:
        print("Wrong answer")
print(f"\nYour total points is {pts}")