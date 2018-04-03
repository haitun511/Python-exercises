game_result = [".O.","...","..."]


def checkio(game_result):

    if ((game_result[1][1] == game_result[0][0] and game_result[1][1] == game_result[2][2]) or \
            (game_result[1][1] == game_result[0][2] and game_result[1][1] == game_result[2][0])) and \
            game_result[1][1] != ".":

        return game_result[1][1]

    else:

        for c in range(3):
            if game_result[c][1] == game_result[c][0] and game_result[c][1] == game_result[c][2] and \
                    game_result[c][1] != ".":

                return game_result[c][1]

            elif game_result[1][c] == game_result[0][c] and game_result[2][c] == game_result[1][c] and \
                    game_result[1][c] != ".":

                return game_result[1][c]

    return "D"


print(checkio(game_result))