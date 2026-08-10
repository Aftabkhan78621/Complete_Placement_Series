arr = [1, 2, 3, 5, 6]

n = len(arr) + 1

xor_all = 0
xor_array = 0

for i in range(1, n + 1):
    xor_all ^= i

for num in arr:
    xor_array ^= num

missing = xor_all ^ xor_array

print(missing)  



def find_missing_number(numbers):

    n = len(numbers) + 1

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


def main():

    numbers = [1, 2, 3, 5, 6]

    print("Missing Number =", find_missing_number(numbers))


if __name__ == "__main__":
    main()