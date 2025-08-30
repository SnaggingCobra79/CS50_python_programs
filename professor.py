import random


def main():
    level = get_level()
    correct = 0
    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        result = a + b
        wrong = 0  # Initialize wrong attempts for each problem
        while wrong < 3:
            try:
                user = int(input(f"{a} + {b} = "))
                if user == result:
                    correct += 1
                    break
                else:
                    print("EEE")
                    wrong += 1
                    if wrong == 3:
                        print(f"{a} + {b} = {result}")
            except ValueError:
                print("EEE")
                wrong += 1
                if wrong == 3:
                    print(f"{a} + {b} = {result}")
    print(correct)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass  # Continue prompting for valid input


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
