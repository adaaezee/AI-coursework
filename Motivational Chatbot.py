def chatbot_greeting(chatbot_name, who_this_is):
    print(f"Hello, I'm {chatbot_name}")
    print(f"your {who_this_is}")
    print("How are you doing today?")

chatbot_greeting("Kelly", "Motivational Bestie")
# This chatbot greets the user and asks how they are doing today.
# It can be used to start a conversation and provide motivation.

# Coversation starter
while True: 
    user_response = input ("Would you like a motivational quote to help improve your mood? (Type 'exit' to quit): ")
    # This loop continues to ask the user if they want a motivational quote until they type 'exit'.
    # If the user types 'exit', the chatbot will say a friendly goodbye and end the conversation

    if user_response.lower() == 'exit':
        print("Goodbye! Stay motivated!")
        break
    elif user_response.lower() in ['yes', 'sure', 'ok', 'please']:
        print("Here's a motivational quote for you:")
        print("'The best preparation for tomorrow is doing your best today.'")
    elif user_response.lower() in ['no', 'not now', 'maybe later', 'nope']:
        print("Okay, have a lovely day! I'm here whenever you need a boost.")
        
        