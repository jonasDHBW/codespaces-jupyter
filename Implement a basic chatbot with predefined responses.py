
import random



def get_response(user_input):

    user_input = user_input.lower()

    responses = {

        "hello": ["Hi there!", "Hello!", "Hey!"],

        "how are you": ["I'm doing well, thanks!", "I'm a chatbot, so I don't have feelings, but I'm here to help!"],

        "goodbye": ["Goodbye!", "See you later!", "Bye!"],

        "default": ["I'm not sure how to respond to that.", "Sorry, I didn't understand. Can you rephrase that?", "I'm just a basic chatbot."]

    }



    for keyword in responses:

        if keyword in user_input:

            return random.choice(responses[keyword])



    return random.choice(responses["default"])



def main():

    print("Welcome to the Basic Chatbot!")

    print("Type 'exit' to end the conversation.")



    while True:

        user_input = input("You: ")

        

        if user_input.lower() == 'exit':

            print("Goodbye!")

            break



        bot_response = get_response(user_input)

        print("Bot:", bot_response)



if __name__ == "__main__":

    main()



