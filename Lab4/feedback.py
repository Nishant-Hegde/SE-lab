def evaluate(target, guess):
    result = ["gray"] * len(guess)
    remaining = {}

    # Count how many occurrences of each letter are in the target
    for ch in target:
        remaining[ch] = remaining.get(ch, 0) + 1

    # First pass: exact matches
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[ch] -= 1

    # Second pass: letters present elsewhere in the target
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result