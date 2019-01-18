def checkGuess(code, guess):
    bulls = cows = 0
    for code_char, guess_char in zip(code, guess):
        if code_char == guess_char:
            bulls = bulls + 1
        elif guess_char in code:
            cows = cows + 1
    return bulls, cows


a = input('select a number : ')
print(checkGuess(a, "4321"))


