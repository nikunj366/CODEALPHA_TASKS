def chatbot_response(user_input):

   
    '''
    taking user input and NovaS response based on the user input.i use if-elif-else statement for the bot response
    '''
    user_input = user_input.strip().lower() # Remove spaces and convert to lowercase

    if user_input == "hello":
        return "Hi! 👋"

    elif user_input == "how are you":
        return "I'm fine, thanks! 😊"

    elif user_input == "what is your name":
        return "I am a Python Chatbot 🤖"

    elif user_input == "bye":
        return "Goodbye! 👋"

    else:
        return "Sorry, I don't understand."



print("=" * 40)
print("🤖 BASIC CHATBOT")
print("Type 'bye' to exit")
print("=" * 40)
while True:

    user = input("\nUser: ")

    response = chatbot_response(user)
    print("Nova:", response)
    if user.strip().lower() == "bye":
        break