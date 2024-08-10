print("Wellcome to quiz game!")
name=input("Enter your name to start the quiz")
score = 0

QUESTIONS = {
    "What is the capital of India?": [
        "Delhi", "Chennai", "Dehradun", "Panaji"
    ],
    "What is the capital of Ankara?": [
        "Turkey","Uruguay","Uganda","Vanuatu"
    ],
    "What is the capital of  Russia": [
        "Moscow", "Delhi","Havana","Prague"
    ],
    "What is the capital of Tanzania?": [ 

        "Dar- es- Salaam","Nairobi","Lusaka","Kampala"
    ],
    "What is the capital of Iran": [
        "Tehran","Riyadh","Kuwait","Khuzestan"
    ],
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        score +=1
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

else:
    print('Thank you for playing.')
    
print(f'Your score is {score}')

