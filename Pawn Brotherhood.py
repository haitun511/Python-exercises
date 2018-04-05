pawns = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}


def safe_pawns(pawns):
    counter = 0

    for pawn in pawns:
        if chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns or \
                chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1) in pawns:
            counter += 1

    return counter


print(safe_pawns(pawns))
