import random

quotes = [
    "Believe in yourself.",
    "Keep pushing forward.",
    "You are stronger than you think.",
    "Every day is a second chance.",
    "The best time to start was yesterday. The next best time is now."
]

def show_random_quote():
    print("\n✨ Here's your motivational quote ✨")
    print(random.choice(quotes))

if __name__ == "__main__":
    show_random_quote()
