
def chatbot():
    print("===== WELCOME TO PYTHON CHATBOT =====")
    print("Hello! I am your chatbot.")
    print("You can chat with me. Type 'bye' to exit.")

    while True:
        user_message = input("\nYou: ").lower().strip()

        if user_message in ["hello", "hi", "hii", "hey", "heyy", "hiii"]:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user_message:
            print("Bot: I'm fine, thanks! How are you?")

        elif "your name" in user_message:
            print("Bot: I am your Python chatbot.")

        elif "python" in user_message:
            print("Bot: Python is a programming language used to build applications and automate tasks.")

        elif "thank" in user_message:
            print("Bot: You're welcome!")

        elif "help" in user_message:
            print("Bot: Sure! Ask me about Python, or just say hello.")

        elif "bye" in user_message or "goodbye" in user_message:
            print("Bot: Goodbye! Have a nice day!")
            break

        elif user_message == "":
            print("Bot: Please type something.")

        else:
            print("Bot: That's interesting! Can you tell me more?")

chatbot()


