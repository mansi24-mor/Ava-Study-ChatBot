import random
from datetime import datetime

print("Namaste! I am Ava! Your Rule based Study ChatBot")
print("You can ask me basic questions.")
print("Type 'bye' to exit.")

# Chatbot memory creation

responses = {
    "hello" : "Hi! Welcome! How can I help you?",
    "how are you" : "I am fine. Thank you!",
    "who are you" : "I am Ava, your study buddy chatbot.",
    "what is your name" : "My name is Ava.",
    "motivate me" : "Keep going. Every bug makes you a better programmer!",
    "happy" : "Great to hear that!",
    "what is python" : "Python is a high-level, interpreted programming language known for its simplicity and readability.",
}

user_name = ""

quiz = {
    "What is the keyword for function in Python?": "def",
    "Which symbol is used for comments in Python?": "#",
    "What keyword is used for loops in Python?": "for",
    "Which data type stores whole numbers in Python?": "int",
    "Which keyword is used for conditions in Python?": "if",
    "Which function is used to take input from users?": "input",
    "Which function is used to display output on screen?": "print",
    "Which loop runs while a condition is true?": "while",
    "Which data type stores text in Python?": "str",
    "Which symbol is used for multiplication in Python?": "*"
}

current_question = ""

# method to get response from Ava
def get_response(user_input):

    global user_name, current_question

    original_input = user_input
    user_input = user_input.lower()

    # Name memory
    if "my name is" in user_input:
        user_name = original_input.replace("my name is","").strip()
        return f"Nice to meet you {user_name}"

    # Time feature
    if "time" in user_input:
        current = datetime.now()
        return f"Current time is {current.strftime('%I:%M %p')}"

    # Quiz feature
    if "quiz" in user_input:
        current_question = random.choice(list(quiz.keys()))
        return current_question

    # Check quiz answer
    if current_question != "":
        correct_answer = quiz[current_question]

        if user_input == correct_answer.lower():
            current_question = ""
            return "Correct answer! Very good!"

        else:
            answer = correct_answer
            current_question = ""
            return f"Wrong answer. Correct answer is: {answer}"

    # OK variations
    if ("ok" in user_input or
        "okay" in user_input or
        "oki" in user_input or
        "ohk" in user_input):
        
        return "Yes 😊"
    
    for each_key in responses:
        if each_key in user_input:
            return responses[each_key]

    return "I am sorry, I don't know this."


# take input from the user

while True:
    user_choice = input("You: ")
    if user_choice == "bye":
        print("Ava: Bye! Have a great day ahead!")
        break
    ava_reply = get_response(user_choice)
    print("Ava: " , ava_reply)
    