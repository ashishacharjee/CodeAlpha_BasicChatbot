import random
import datetime
import math

# ─────────────────────────────────────────────
#  Bot Configuration
# ─────────────────────────────────────────────
BOT_NAME    = "CodeBot"
BOT_VERSION = "2.0"

# Stores the user's name once they tell us
user_name       = None
conversation_log = []
mood            = "neutral"   # neutral | happy | sad


# ─────────────────────────────────────────────
#  Response bank
# ─────────────────────────────────────────────
RESPONSES = {
    "greeting": {
        "triggers": ["hello", "hi", "hey", "howdy", "hiya", "good morning", "good evening", "good afternoon", "sup", "what's up"],
        "replies":  ["Hey {name}! How can I help you today?",
                     "Hello {name}! Great to see you 😊",
                     "Hi {name}! What's on your mind?"],
    },
    "how_are_you": {
        "triggers": ["how are you", "how are you doing", "how's it going", "you okay", "how do you do", "are you fine"],
        "replies":  ["I'm doing great, thanks for asking {name}!",
                     "All good on my end! How about you, {name}?",
                     "Feeling fantastic as always! What about you?"],
    },
    "name_ask": {
        "triggers": ["what is your name", "what's your name", "who are you", "your name", "introduce yourself"],
        "replies":  [f"I'm {BOT_NAME}, your Python-powered assistant! 🤖",
                     f"They call me {BOT_NAME}. Nice to meet you!"],
    },
    "user_name": {
        "triggers": ["my name is", "i am", "call me", "i'm"],
        "replies":  ["Nice to meet you, {name}! I'll remember that 😊",
                     "Got it! I'll call you {name} from now on."],
    },
    "age": {
        "triggers": ["how old are you", "your age", "what is your age"],
        "replies":  ["I was born the moment my first line of Python was written — so age is complicated!",
                     "Technically I'm as old as my last `git commit` 😄"],
    },
    "joke": {
        "triggers": ["joke", "tell me a joke", "make me laugh", "funny", "say something funny"],
        "replies":  [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the Python programmer get lost? He took too many wrong turns in the loop!",
            "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
            "Why is Python so good at music? Because it knows all the scales!",
            "What do you call a bear with no teeth? A gummy bear — just like runtime errors, soft but painful 😄",
        ],
    },
    "time": {
        "triggers": ["time", "what time is it", "current time", "tell me the time"],
        "replies":  [],   # handled dynamically
    },
    "date": {
        "triggers": ["date", "today's date", "what day is it", "current date", "what is today"],
        "replies":  [],   # handled dynamically
    },
    "weather": {
        "triggers": ["weather", "is it raining", "temperature outside"],
        "replies":  ["I'm just a text bot so I can't check live weather, but try weather.com or just ask Google! 🌤"],
    },
    "python": {
        "triggers": ["python", "do you like python", "python programming", "tell me about python"],
        "replies":  [
            "Python is awesome — clean syntax, powerful libraries, what's not to love? 🐍",
            "Python is literally my native language! Indentation is everything.",
            "I was built with Python! It's beginner-friendly yet incredibly powerful.",
        ],
    },
    "codealpha": {
        "triggers": ["codealpha", "code alpha", "your company", "internship"],
        "replies":  ["CodeAlpha is a great platform for learning! Check them out at www.codealpha.tech 🚀"],
    },
    "help": {
        "triggers": ["help", "what can you do", "commands", "options", "menu"],
        "replies":  [],   # handled dynamically
    },
    "thanks": {
        "triggers": ["thank you", "thanks", "thx", "thank you so much", "ty"],
        "replies":  ["You're welcome {name}! 😊",
                     "Happy to help, {name}!",
                     "Anytime! That's what I'm here for."],
    },
    "sad": {
        "triggers": ["i am sad", "i'm sad", "feeling down", "i feel bad", "i'm upset", "not okay", "depressed"],
        "replies":  [
            "I'm sorry to hear that {name}. Remember, tough times don't last 💙",
            "Hey {name}, it's okay to feel that way. Want to talk about it, or shall I tell you a joke to cheer you up?",
            "Sending virtual good vibes your way {name} 🌟 Things will get better!",
        ],
    },
    "happy": {
        "triggers": ["i am happy", "i'm happy", "feeling great", "i feel good", "i'm excited", "awesome", "amazing"],
        "replies":  [
            "That's wonderful {name}! Keep that energy going! 🎉",
            "Love to hear it {name}! What's got you in such a great mood?",
            "Yay {name}! Happy vibes are the best vibes! 😄",
        ],
    },
    "math": {
        "triggers": ["calculate", "what is", "solve", "math", "compute"],
        "replies":  [],   # handled dynamically
    },
    "bye": {
        "triggers": ["bye", "goodbye", "see you", "exit", "quit", "take care", "see ya", "farewell"],
        "replies":  ["Goodbye {name}! Have a wonderful day! 👋",
                     "See you later {name}! Take care.",
                     "Bye {name}! Come back anytime 😊"],
    },
}

QUIZ_QUESTIONS = [
    {"q": "What does CPU stand for?",                    "a": "central processing unit"},
    {"q": "Which language is known as the mother of all languages?", "a": "c"},
    {"q": "What does HTML stand for?",                   "a": "hypertext markup language"},
    {"q": "What symbol starts a comment in Python?",     "a": "#"},
    {"q": "How many bits are in a byte?",                "a": "8"},
    {"q": "What does OOP stand for?",                    "a": "object oriented programming"},
    {"q": "Which data structure uses LIFO?",             "a": "stack"},
]

exit_triggers = RESPONSES["bye"]["triggers"]


# ─────────────────────────────────────────────
#  Feature handlers
# ─────────────────────────────────────────────
def get_time_response():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')} 🕐"


def get_date_response():
    now = datetime.datetime.now()
    return f"Today is {now.strftime('%A, %d %B %Y')} 📅"


def get_help_response():
    return (
        f"\n  Here's what I can do, {{name}}:\n"
        "  • Chat — greetings, how are you, jokes, mood support\n"
        "  • Info  — time, date, Python facts, CodeAlpha info\n"
        "  • Math  — type 'calculate 25 * 4' or 'sqrt 144'\n"
        "  • Quiz  — type 'quiz' to test your knowledge\n"
        "  • History — type 'history' to see our conversation\n"
        "  • Clear — type 'clear' to reset chat history\n"
        "  • Bye   — type 'bye' to exit\n"
    )


def try_math(text):
    """Try to evaluate a math expression from the user's input."""
    text = text.lower().replace("calculate", "").replace("what is", "").replace("solve", "").replace("compute", "").strip()

    # Handle sqrt
    if text.startswith("sqrt"):
        try:
            num = float(text.replace("sqrt", "").strip())
            return f"√{num} = {math.sqrt(num):.4f}"
        except Exception:
            return None

    # Handle power
    text = text.replace("^", "**").replace("×", "*").replace("÷", "/")

    try:
        # Only allow safe characters
        allowed = set("0123456789 +-*/.%()")
        if all(c in allowed for c in text):
            result = eval(text)
            return f"{text} = {result}"
    except Exception:
        pass
    return None


def run_quiz():
    question = random.choice(QUIZ_QUESTIONS)
    print(f"\n  🧠 Quiz Time!")
    print(f"  Q: {question['q']}")
    answer = input("  Your answer: ").strip().lower()

    if answer == question["a"].lower():
        return "  ✅ Correct! Well done! 🎉"
    else:
        return f"  ❌ Not quite! The answer was: '{question['a'].title()}'"


def extract_name(text):
    """Try to extract a name from phrases like 'my name is X' or 'I am X'."""
    phrases = ["my name is ", "i am ", "call me ", "i'm "]
    text_lower = text.lower()
    for phrase in phrases:
        if phrase in text_lower:
            after = text_lower.split(phrase, 1)[1].strip()
            name = after.split()[0].capitalize() if after else None
            return name
    return None


def format_reply(reply, name):
    display = name if name else "friend"
    return reply.replace("{name}", display)


def log(role, message):
    ts = datetime.datetime.now().strftime("%H:%M")
    conversation_log.append({"time": ts, "role": role, "message": message})


def show_history():
    if not conversation_log:
        return "  No conversation history yet."
    lines = ["\n  ─── Conversation History ─────────────────"]
    for entry in conversation_log[-20:]:  # last 20 messages
        label = "You     " if entry["role"] == "user" else BOT_NAME
        lines.append(f"  [{entry['time']}] {label}: {entry['message']}")
    lines.append("  ──────────────────────────────────────────")
    return "\n".join(lines)


# ─────────────────────────────────────────────
#  Core response engine
# ─────────────────────────────────────────────
def get_response(user_input):
    global user_name

    text = user_input.lower().strip()

    # Special commands
    if text == "quiz":
        return run_quiz()

    if text == "history":
        return show_history()

    if text == "clear":
        conversation_log.clear()
        return "  Chat history cleared! Fresh start 🧹"

    # Math
    if any(kw in text for kw in RESPONSES["math"]["triggers"]):
        result = try_math(text)
        if result:
            return f"  🔢 {result}"

    # Name extraction
    extracted = extract_name(text)
    if extracted:
        user_name = extracted
        reply = random.choice(RESPONSES["user_name"]["replies"])
        return format_reply(reply, user_name)

    # Time / Date (dynamic)
    if any(t in text for t in RESPONSES["time"]["triggers"]):
        return get_time_response()

    if any(t in text for t in RESPONSES["date"]["triggers"]):
        return get_date_response()

    if any(t in text for t in RESPONSES["help"]["triggers"]):
        return format_reply(get_help_response(), user_name)

    # General responses
    for category, data in RESPONSES.items():
        if category in ("math", "time", "date", "help", "user_name"):
            continue
        for trigger in data["triggers"]:
            if trigger in text:
                reply = random.choice(data["replies"])
                return format_reply(reply, user_name)

    # Fallback
    fallbacks = [
        "Hmm, I'm not sure about that {name}. Type 'help' to see what I can do!",
        "I didn't quite catch that, {name}. Try rephrasing or type 'help'.",
        "Interesting! But I'm still learning. Type 'help' to see my features 😊",
    ]
    return format_reply(random.choice(fallbacks), user_name)


def is_exit(text):
    return any(t in text.lower() for t in exit_triggers)


# ─────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────
def main():
    print("\n" + "═" * 46)
    print(f"   {BOT_NAME} v{BOT_VERSION} — CodeAlpha Python Internship")
    print("═" * 46)
    print(f"  Hi! I'm {BOT_NAME} 🤖  Type 'help' to see what I can do.")
    print("  Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("  You      : ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n  {BOT_NAME}: Goodbye! 👋\n")
            break

        if not user_input:
            print(f"  {BOT_NAME}: Say something! I'm listening 😊\n")
            continue

        log("user", user_input)
        reply = get_response(user_input)
        print(f"  {BOT_NAME}: {reply}\n")
        log("bot", reply)

        if is_exit(user_input):
            break


if __name__ == "__main__":
    main()
