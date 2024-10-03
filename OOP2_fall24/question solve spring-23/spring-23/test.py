def demo():
    while True:
        user_input = input("You: ")
        if "hi" == user_input.lower():
            print("ChatGPT: Hi! What can I do now?")
        elif "do you know me" == user_input.lower():
            print("ChatGPT: You are from Daffodil International University. You are currently in the 5th semester.")
        elif "thanks for you information" == user_input.lower():
            print("ChatGPT: Thanks for your gratitude.")
        elif "exit" in user_input.lower():
            print("ChatGPT: Goodbye!")
            break
        else:
            print("ChatGPT: Sorry, I don't understand that.")
demo()

