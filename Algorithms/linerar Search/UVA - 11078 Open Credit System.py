def max_difference(arr):
    max_diff = float('-inf')
    max_value = arr[0]

    for i in range(1, len(arr)):
        diff = max_value - arr[i]
        max_diff = max(max_diff, diff)
        max_value = max(max_value, arr[i])

    return max_diff


def main():
    test_cases = int(input().strip())

    for _ in range(test_cases):
        n = int(input().strip())
        grades = [int(input().strip()) for _ in range(n)]

        result = max_difference(grades)
        print(result)


if __name__ == "__main__":
    main()
