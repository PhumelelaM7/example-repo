"""Recursive function to find the largest number in a list."""


def largest_number(numbers):
    """Recursively find the largest number in a list."""
    # Defensive programming.
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")

    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers.")

    # Base case: only one element.
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case.
    # Compare first element with the largest of the rest.
    max_of_rest = largest_number(numbers[1:])

    if numbers[0] > max_of_rest:
        return numbers[0]
    return max_of_rest


def main():
    """Main program to test the function."""
    try:
        result_1 = largest_number([1, 4, 5, 3])
        # Expected 5.
        print("Example 1 result:", result_1)

        result_2 = largest_number([3, 1, 6, 8, 2, 4, 5])
        # Expected 8.
        print("Example 2 result:", result_2)

    except (TypeError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
