"""
Typing Speed Test (CLI)

Type the given sentence and get WPM and accuracy.

Usage:
Run the script and follow instructions.

"""

import time

def typing_test(text):
    print("Type the following sentence:\n")
    print(text)
    input("Press Enter to start...")
    start = time.time()
    typed = input()
    end = time.time()

    time_taken = end - start
    words = typed.split()
    total_words = len(text.split())
    correct_words = sum(1 for i, word in enumerate(typed.split()) if i < total_words and word == text.split()[i])
    accuracy = correct_words / total_words * 100
    wpm = len(words) / (time_taken / 60)
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog."
    typing_test(sample_text)
