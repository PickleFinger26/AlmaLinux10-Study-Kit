#!/usr/bin/env python3
"""Interactive offline flashcard quiz; standard library only."""
import argparse
import json
import random
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="LinuxZoo flashcard revision")
    parser.add_argument("--lesson", help="Filter by lesson ID, e.g. SELinux1")
    parser.add_argument("--count", type=int, default=10, help="Number of random cards")
    parser.add_argument("--list-lessons", action="store_true")
    args = parser.parse_args()
    cards = json.loads((Path(__file__).resolve().parent.parent / "data/flashcards.json").read_text())
    if args.list_lessons:
        print(", ".join(dict.fromkeys(c["lesson"] for c in cards)))
        return
    if args.lesson:
        cards = [c for c in cards if c["lesson"].lower() == args.lesson.lower()]
    if not cards:
        parser.error("No cards for this lesson; use --list-lessons")
    selected = random.sample(cards, min(max(1, args.count), len(cards)))
    correct = 0
    for index, card in enumerate(selected, 1):
        print(f"\n[{index}/{len(selected)}] ({card['lesson']}) {card['question']}")
        try:
            input("Think of your answer. Press Enter to reveal… ")
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz ended.")
            return
        print("Answer:", card["answer"])
        try:
            result = input("Did you get it right? [y/N] ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz ended.")
            return
        correct += result in ("y", "yes")
    print(f"\nSelf-scored result: {correct}/{len(selected)} ({correct / len(selected):.0%}).")

if __name__ == "__main__":
    main()
