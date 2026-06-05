"""
Simple Python Chatbot
Run: python chatbot.py
"""

responses = {
    "hello": "Hey there! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm SimpleBot, your friendly chatbot!",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer basic questions. Try: hello, how are you, what is your name, joke, time",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "time": None,  # handled dynamically
}

def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("bye", "exit", "quit"):
        return "Goodbye! 👋", True

    if text == "time":
        from datetime import datetime
        return f"Current time: {datetime.now().strftime('%H:%M:%S')}", False

    for key, reply in responses.items():
        if key in text:
            return reply, False

    return "I'm not sure how to respond to that. Type 'help' for options.", False


def main():
    print("=" * 40)
    print("      Welcome to SimpleBot 🤖")
    print("   Type 'bye' or 'quit' to exit")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue

        reply, should_exit = get_response(user_input)
        print(f"Bot: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    main()
