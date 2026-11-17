
def calculate_average(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(number)

    return average


def main():
    numbers = [10, 20, 30, 40, 50]

    result = calculate_average(numbers)

    print("Average:", result)

    print("Total:", total)


if __name__ == "__main__":
    main()
