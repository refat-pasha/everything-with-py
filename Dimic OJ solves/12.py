

def count_trailing_zeros(N):
    count = 0
    power_of_5 = 5
    while N >= power_of_5:
        count += N // power_of_5
        power_of_5 *= 5
    return count

# Read number of test cases
T = int(input())
results = []

# Process each test case
for _ in range(T):
    N = int(input())
    results.append(count_trailing_zeros(N))

# Print results for each test case
for result in results:
    print(result)
