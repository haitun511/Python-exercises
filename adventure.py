class Room:

    def __init__(self, column_start, column_end, row_start, row_end, color):
        self.column_range = range(column_start, column_end + 1)
        self.row_range = range(row_start, row_end + 1)
        self.color = color


def get_direction(direction, current_row, current_column):

    if direction == "L":
        potential_column = current_column - 1
        potential_row = current_row

    elif direction == "R":
        potential_column = current_column + 1
        potential_row = current_row

    elif direction == "U":
        potential_row = current_row - 1
        potential_column = current_column

    elif direction == "D":
        potential_row = current_row + 1
        potential_column = current_column

    else:
        print("Type 'Q' to quit. Otherwise, type your direction for the next move.")

    return potential_row, potential_column


def check_position(potential_row, potential_column, rooms):

    in_status = False

    for room in rooms:
        if potential_column in room.column_range and potential_row in room.row_range:
            room_description = room.color
            in_status = True
            return in_status, room_description

    return in_status, ""    


def movement(potential_row, potential_column):
    current_column = potential_column
    current_row = potential_row
    return current_row, current_column


def current_position(current_row, current_column, room_description):
    print("Your current position is ({0}, {1}).".format(current_row, current_column))
    print("You are in the {0} room.".format(room_description))


def main():

    orange_room = Room(1, 4, 1, 12, "orange")
    brown_room = Room(1, 2, 13, 21, "brown")
    red_room = Room(4, 5, 13, 19, "red")
    blue_room = Room(7, 9, 3, 17, "blue")
    grey_room = Room(5, 6, 7, 12, "grey")
    green_room = Room(3, 3, 16, 19, "green")

    rooms = [orange_room, blue_room, brown_room, red_room, green_room, grey_room]

    current_column = 1
    current_row = 1
    direction = input("Next Move Direction: ")

    while direction != "Q":
        potential_row, potential_column = get_direction(direction, current_row, current_column)
        in_status, room_description = check_position(potential_row, potential_column, rooms)

        while not in_status:
            print("You are not allowed to go to that direction.")
            direction = input("Next Move Direction: ")
            potential_row, potential_column = get_direction(direction, current_row, current_column)
            in_status, room_description = check_position(potential_row, potential_column, rooms)

        current_row, current_column = movement(potential_row, potential_column)
        current_position(current_row, current_column, room_description)
        direction = input("Next Move Direction: ")
        get_direction(direction, current_row, current_column)


main()
