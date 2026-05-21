# CodeBot — Python Chatbot 🤖

A smart rule-based chatbot built with Python as part of the **CodeAlpha Python Programming Internship**.

## How to Run

```bash
python chatbot.py
```

> No external libraries needed. Works with Python 3.x out of the box.

## Features

- **Remembers Your Name** — Tell it your name and it uses it throughout the conversation
- **Math Calculator** — Handles arithmetic and square roots (e.g. `calculate 25 * 4`, `sqrt 144`)
- **Quiz Mode** — Type `quiz` to get a random tech/CS trivia question
- **Conversation History** — Type `history` to view the last 20 messages with timestamps
- **Clear History** — Type `clear` to reset the conversation log
- **Mood Detection** — Responds differently if you say you're happy or sad
- **Time & Date** — Tells you the current time and today's date
- **Joke Generator** — Multiple jokes, randomly picked each time
- **Help Menu** — Type `help` to see all available commands
- **Graceful Exit** — Type `bye`, `quit`, or `goodbye` to exit

## What It Can Handle

| Topic | Example Input |
|---|---|
| Greetings | `hello`, `hey`, `good morning` |
| Name | `my name is Ashish` |
| How are you | `how are you`, `how's it going` |
| Jokes | `tell me a joke`, `make me laugh` |
| Math | `calculate 12 * 8`, `sqrt 256` |
| Time & Date | `what time is it`, `today's date` |
| Quiz | `quiz` |
| Mood | `i'm feeling sad`, `i'm happy` |
| History | `history` |
| Help | `help`, `what can you do` |
| Exit | `bye`, `goodbye`, `quit` |

## Sample Conversation

```
You      : my name is Ashish
CodeBot  : Nice to meet you, Ashish! I'll remember that 😊

You      : calculate 15 * 6
CodeBot  : 🔢 15 * 6 = 90

You      : quiz
CodeBot  : 🧠 Quiz Time!
           Q: How many bits are in a byte?
You      : 8
CodeBot  : ✅ Correct! Well done! 🎉

You      : bye
CodeBot  : Goodbye Ashish! Have a wonderful day! 👋
```

## Concepts Used

`if-elif`, functions, loops, dictionaries, `random`, `datetime`, `math`, input/output

## Project Structure

```
CodeAlpha_BasicChatbot/
└── chatbot.py
```

## Internship Details

- **Organization:** CodeAlpha
- **Domain:** Python Programming
- **Student ID:** CA/DF1/75758
- **Duration:** 20th May 2026 – 20th June 2026
