import random

answer = random.randint(1, 41)


def give_hint(i):
    def number_one():
        hint_range = ""
        if answer < 10:
            hint_range = "1-10"
        elif answer < 20:
            hint_range = "10-20"
        elif answer < 30:
            hint_range = "20-30"
        else:
            hint_range = "30-40"
        print("The number is between " + hint_range + ".")

    def number_two():
        if answer % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

    digits = len(str(answer))

    def number_three():
        if digits == 1:
            print("The number has 1 digit.")
        else:
            print("The number has 2 digits.")

    if i == 1:
        number_one()
    if i == 2:
        number_two()
    if i == 3:
        number_three()


def main():
    hint_count = 1
    users_answer = ""
    while answer != users_answer and hint_count < 4:
        give_hint(hint_count)
        users_answer = input("Now guess the number!")
        users_answer = int(users_answer)
        if answer == users_answer:
            print("You got the correct answer!")
        else:
            print("Wrong answer!")
        hint_count += 1
    print("The game is over. The answer is " + str(answer) + ".")


if __name__ == "__main__":
    print(
        "This is a guessing game and you will type the number you think based on the hint. "
        "If it is wrong, you will have another hint. Have fun!"
    )
    main()
