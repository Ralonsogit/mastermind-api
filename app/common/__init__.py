def get_feedback(code, guess):
    white_pegs, black_pegs = 0, 0
    indexes = set()

    if guess == code:
        return '40'

    for i in range(len(code)):
        if code[i] == guess[i]:
            white_pegs += 1
            indexes.add(i)
        else:
            contains = [x for x, code_ch in enumerate(code) if code_ch == guess[i]]
            if contains:
                for g in contains:
                    if g not in indexes:
                        black_pegs += 1
                        indexes.add(g)
    return white_pegs, black_pegs
