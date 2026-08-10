# # Question

# Given a sorted array of employee IDs, remove duplicate IDs in-place while preserving the original order.

# Conditions:
# • Don't use set().
# • Don't create another array of the same size.
# • Use Two Pointer technique.

# Example:
# Input: [101, 101, 102, 103, 103, 104, 105, 105]

# Output:
# [101, 102, 103, 104, 105]

# # Answer (Approach)

# • Since the array is sorted, duplicate elements are consecutive.
# • Use two pointers:
#   - write → Position to place the next unique element.
#   - read → Scans the entire array.
# • Whenever arr[read] != arr[write], move write forward and copy the unique element.

# # Algorithm

# 1. If the array is empty, return [].
# 2. Initialize write = 0.
# 3. Traverse the array using read from index 1.
# 4. If arr[read] != arr[write]:
#    • Increment write.
#    • Copy arr[read] to arr[write].
# 5. The unique elements are stored from index 0 to write.

# # Python Code

# arr = [101, 101, 102, 103, 103, 104, 105, 105]

# if not arr:
#     print([])
# else:
#     write = 0

#     for read in range(1, len(arr)):
#         if arr[read] != arr[write]:
#             write += 1
#             arr[write] = arr[read]

#     for i in range(write + 1):
#         print(arr[i], end=" ")

# # Important Points

# • Array must be sorted.
# • Duplicates are consecutive.
# • First element is always unique.
# • read scans the array.
# • write stores the next unique element.
# • No extra array is used.

# # Edge Cases

# Input: []
# Output: []

# Input: [5]
# Output: [5]

# Input: [1, 1, 1, 1]
# Output: [1]

# Input: [1, 2, 3, 4]
# Output: [1, 2, 3, 4]

# # Time Complexity

# O(n)

# # Space Complexity

# O(1)

# # Follow-up Questions

# • Remove Duplicates II.
# • Remove Element.
# • Move Zeroes.
# • Merge Sorted Arrays.
# • Two Sum II.

# # Pattern Recognition

# Keywords:
# • Sorted Array
# • Remove Duplicates
# • In-place
# • O(1) Space

# ➡️ Think Two Pointer Technique.


def remove_duplicates(orders):

    if not orders:
        return 0, []

    write = 0

    for read in range(1, len(orders)):

        if orders[read] != orders[write]:
            write += 1
            orders[write] = orders[read]

    return write + 1, orders[:write + 1]


def main():

    orders = [101, 101, 102, 103, 103, 104, 105, 105]

    unique_count, unique_orders = remove_duplicates(orders)

    print("Unique Count =", unique_count)
    print("Unique Orders =", unique_orders)


if __name__ == "__main__":
    main()