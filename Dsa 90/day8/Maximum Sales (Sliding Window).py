def maximum_sales(sales, k):

    window_sum = sum(sales[:k])
    max_sum = window_sum

    for i in range(k, len(sales)):
        window_sum = window_sum - sales[i - k] + sales[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def main():

    sales = [2, 5, 1, 8, 2, 9, 1]
    k = 3

    print("Maximum Sales =", maximum_sales(sales, k))


if __name__ == "__main__":
    main()