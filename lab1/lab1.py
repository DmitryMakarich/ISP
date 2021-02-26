def fibonacci(number):
    if number <= 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


def main():
    try:
        number = int(input("Input number: "))
        print(fibonacci(number))
    except ValueError:
        print("Incorrect input")


if __name__ == '__main__':
    main()
