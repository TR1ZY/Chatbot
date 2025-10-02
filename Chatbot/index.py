while True:
    user_input: str = input('You: ')

    if user_input == 'Hello':
        print('Bot: Hello!')
    elif user_input == 'How are you!':
        print('Bot: Good, how about you?')
    elif user_input == 'bye':
        print('Bot: Goodbye!')
    else:
        print('Bot: Sorry, I did not understand that.')