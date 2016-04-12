import random


def stay():
    countstay = 0
    loss = 0

    for _ in range(0, 1000):
        listy = [0, 1, 2]
        winner = random.choice(listy)
        first_choice = random.choice(listy)

        if winner == first_choice:
            countstay += 1
        else:
            loss += 1

    print("stayed loss", loss)
    print("stayed winner", countstay)


def switch():
    countswitch = 0
    loss = 0

    for _ in range(0, 1000):
        listy = [0, 1, 2]
        winner = random.choice(listy)
        first_choice = random.choice(listy)
        listy.pop(first_choice)

        if first_choice == winner:
            listy.pop(listy.index(random.choice(listy)))
        else:
            new_list = [0, 1, 2]
            new_list.remove(first_choice)
            new_list.remove(winner)
            listy.remove(new_list[0])

        second_choice = random.choice(listy)

        if second_choice == winner:
            countswitch += 1
        else:
            loss += 1

    print("switch win", countswitch)
    print("switch loss", loss)


def main():
    stay()
    switch()

if __name__ == '__main__':
    main()
