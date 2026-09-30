from game import WordleGame


if __name__ == "__main__":
    print("Choose word length:")
    print("4 - Four-letter word")
    print("5 - Five-letter word")
    print("6 - Six-letter word")

    while True:
        choice = input("Enter 4, 5, or 6: ").strip()

        if choice in {"4", "5", "6"}:
            length = int(choice)
            break

        print("Invalid choice. Enter 4, 5, or 6.")

    WordleGame(length).run()