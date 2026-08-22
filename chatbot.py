import datetime

print("=== Ruled-Based AI Chatbot ===")
print("Type 'help' to see commands, or type 'bye' to exit.")

while True:
    user_input = input("You: ")

    # Clean the user input
    user_input = user_input.strip().lower()
    user_input = user_input.replace("!", "")
    user_input = user_input.replace("?", "")
    user_input = user_input.replace(".", "")
    user_input = user_input.replace(",", "")
    user_input = user_input.replace("'", "")

    # If user presses Enter without typing anything
    if user_input == "":
        print("Bot: Please type something. Type 'help' for commands.")
        continue

    # Greetings
    if user_input in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:
        print("Bot: Hello! I am PyBot. Type 'help' to see what I can answer.")

    # Exit commands
    elif user_input in [
        "bye",
        "exit",
        "quit",
        "goodbye",
        "good night"
    ]:
        print("Bot: Goodbye! It was nice chatting with you.")
        break

    # Help command
    elif user_input in ["help", "what can you do"]:
        print("Bot: Here are some things you can say:")
        print("- hello / hi / hey")
        print("- good morning / good afternoon / good evening")
        print("- bye / exit / quit / goodbye / good night")
        print("- how are you")
        print("- what is your name")
        print("- who made you")
        print("- joke / fact / tell me a story")
        print("- time / date")
        print("- what is ai / what is python")
        print("- favorite color / favorite food / favorite animal")
        print("- favorite subject / favorite game / hobby")
        print("- where are you from / where do you live")
        print("- are you a robot / are you real")
        print("- how old are you")
        print("- motivate me")
        print("- what is 2+2 / what is 5+5")
        print("- thank you / sorry")
        print("- quiz / ask me a question")

    # Ask how the bot is doing
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I am doing very well, thank you for asking!")

    # Bot name
    elif user_input in ["what is your name", "whats your name", "your name"]:
        print("Bot: My name is PyBot, a simple rule-based chatbot.")

    # Creator
    elif user_input in ["who made you", "who created you"]:
        print("Bot: I was created by a Python learner using if-elif-else rules.")

    # Joke
    elif user_input in ["joke", "tell me a joke"]:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Fact
    elif user_input in ["fact", "tell me a fact"]:
        print("Bot: A rule-based chatbot follows programmed rules instead of learning from data.")

    # Story
    elif user_input in ["tell me a story", "story"]:
        print("Bot: Once upon a time, a small Python chatbot learned to talk with humans and help them practice Python.")

    # Time
    elif user_input in ["time", "what time is it"]:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Date
    elif user_input in ["date", "what is the date"]:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        print(f"Bot: Today's date is {current_date}.")

    # AI explanation
    elif user_input in ["what is ai", "ai"]:
        print("Bot: AI stands for Artificial Intelligence, which means making computers perform smart tasks.")

    # Python explanation
    elif user_input in ["what is python", "python"]:
        print("Bot: Python is a beginner-friendly programming language that is easy to read and powerful.")

    # Favorite color
    elif user_input in [
        "favorite color",
        "what is your favorite color",
        "whats your favorite color"
    ]:
        print("Bot: My favorite color is blue, like the Python logo.")

    # Favorite food
    elif user_input in [
        "favorite food",
        "what is your favorite food",
        "whats your favorite food"
    ]:
        print("Bot: My favorite food is data bytes!")

    # Favorite animal
    elif user_input in [
        "favorite animal",
        "what is your favorite animal",
        "whats your favorite animal"
    ]:
        print("Bot: My favorite animal is a Python, of course!")

    # Favorite subject
    elif user_input in [
        "favorite subject",
        "what is your favorite subject",
        "whats your favorite subject"
    ]:
        print("Bot: My favorite subject is computer science.")

    # Favorite game
    elif user_input in [
        "favorite game",
        "what is your favorite game",
        "whats your favorite game"
    ]:
        print("Bot: I like guessing games and Python quizzes.")

    # Hobby
    elif user_input in [
        "hobby",
        "what is your hobby",
        "whats your hobby",
        "what are your hobbies"
    ]:
        print("Bot: My hobby is answering questions quickly and helping you learn Python.")

    # Where the bot is from / where it lives
    elif user_input in ["where are you from", "where do you live"]:
        print("Bot: I live inside your Python program.")

    # Are you a robot / real
    elif user_input in ["are you a robot", "are you real"]:
        print("Bot: I am a rule-based chatbot, not a human.")

    # Age
    elif user_input in [
        "how old are you",
        "what is your age",
        "whats your age",
        "age"
    ]:
        print("Bot: I am only as old as this Python program.")

    # Motivation
    elif user_input in ["motivate me", "motivation"]:
        print("Bot: Keep practicing! Every expert programmer started with small projects like this one.")

    # Simple math: 2+2
    elif user_input in ["what is 2+2", "2+2"]:
        print("Bot: 2 + 2 = 4")

    # Simple math: 5+5
    elif user_input in ["what is 5+5", "5+5"]:
        print("Bot: 5 + 5 = 10")

    # Thank you
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You are welcome!")

    # Sorry
    elif user_input in ["sorry"]:
        print("Bot: No problem. I am happy to help.")

    # Mini quiz
    elif user_input in ["quiz", "ask me a question"]:
        score = 0
        print("Bot: Let's play a Python quiz!")

        answer1 = input("Bot: Question 1: What keyword creates a loop that repeats while a condition is true? ")
        if answer1.strip().lower() == "while":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Incorrect. The correct answer is 'while'.")

        answer2 = input("Bot: Question 2: What symbol checks if two values are equal in Python? ")
        if answer2.strip().lower() == "==":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Incorrect. The correct answer is '=='.")

        answer3 = input("Bot: Question 3: What keyword runs code only when a condition is true? ")
        if answer3.strip().lower() == "if":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Incorrect. The correct answer is 'if'.")

        print(f"Bot: Quiz finished! Your score is {score}/3.")

    # Unknown command
    else:
        print("Bot: Sorry, I do not understand that. Type 'help' to see supported commands.")