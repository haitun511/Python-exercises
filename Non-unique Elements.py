def check(lst):
    for number in set(lst):
        if lst.count(number) == 1:
            lst.remove(number)

    return lst
