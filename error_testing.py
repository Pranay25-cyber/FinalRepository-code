def calculate_average(numbers):
    if not numbers:
        return 0, 0

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return average, total


def main():
    numbers = [10, 20, 30, 40, 50]

    result, total = calculate_average(numbers)

    print("Average:", result)

    print("Total:", total)


if __name__ == "__main__":
    main()
    print("Testing AI Code Review Agent")
