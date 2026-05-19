import random
import datetime

responses = {
    "greeting": {
        "triggers": ["hello", "hi", "hey", "howdy", "good morning", "good evening", "good afternoon"],
        "replies": [
            "Hey there! How can I help you?",
            "Hello! Great to see you.",
            "Hi! What's on your mind?",
        ],
    },
    "how_are_you": {
        "triggers": ["how are you", "how are you doing", "how's it going", "you okay", "how do you do"],
        "replies": [
            "I'm doing great, thanks for asking!",
            "All good on my end! How about you?",
            "I'm just a bot, but I'm feeling fantastic!",
        ],
    },
    "name": {
        "triggers": ["what is your name", "what's your name", "who are you", "your name"],
        "replies": [
            "I'm CodeBot, your Python-powered assistant!",
            "The name's CodeBot. Nice to meet you!",
        ],
    },
    "joke": {
        "triggers": ["joke", "tell me a joke", "make me laugh", "say something funny"],
        "replies": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the Python programmer get lost? He took too many wrong turns in the loop!",
            "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
        ],
    },
    "time": {
        "triggers": ["time", "what time is it", "current time"],
        "replies": [f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."],
    },
    "date": {
        "triggers": ["date", "today's date", "what day is it", "current date"],
        "replies": [f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}."],
    },
    "thanks": {
        "triggers": ["thank you", "thanks", "thx", "thank you so much"],
        "replies": ["You're welcome!", "Happy to help!", "Anytime!"],
    },
    "python": {
        "triggers": ["python", "do you like python", "python programming"],
        "replies": [
            "Python is awesome — clean syntax, powerful libraries, what's not to love?",
            "Python is literally my native language!",
        ],
    },
    "help": {
        "triggers": ["help", "what can you do", "commands"],
        "replies": [
            "I can chat about: greetings, jokes, the time, Python, and more. Just talk to me!",
        ],
    },
    "bye": {
        "triggers": ["bye", "goodbye", "see you", "exit", "quit", "take care"],
        "replies": ["Goodbye! Have a great day!", "See you later!", "Bye! Come back anytime."],
    },
}

exit_triggers = responses["bye"]["triggers"]


def get_response(user_input):
    text = user_input.lower().strip()
    for category, data in responses.items():
        for trigger in data["triggers"]:
            if trigger in text:
                return random.choice(data["replies"])
    fallbacks = [
        "Hmm, I'm not sure about that. Try asking something else!",
        "I didn't quite get that. You can ask me for a joke, the time, or just say hi!",
        "Still learning! Try asking 'what can you do' to see what I know.",
    ]
    return random.choice(fallbacks)


def is_exit(user_input):
    text = user_input.lower().strip()
    return any(trigger in text for trigger in exit_triggers)


def main():
    print("\n" + "=" * 42)
    print("    CodeAlpha — CodeBot (Python Chatbot)")
    print("=" * 42)
    print(" Type anything to chat. Type 'bye' to exit.\n")

    while True:
        user_input = input(" You: ").strip()

        if not user_input:
            print(" CodeBot: Say something! I'm listening.\n")
            continue

        reply = get_response(user_input)
        print(f" CodeBot: {reply}\n")

        if is_exit(user_input):
            break


if __name__ == "__main__":
    main()
