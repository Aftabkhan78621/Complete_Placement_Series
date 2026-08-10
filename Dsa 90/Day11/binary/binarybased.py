# 1. Binary Search

def binary_search(book_ids, target):

    left = 0
    right = len(book_ids) - 1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            return mid

        elif book_ids[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# 2. First Occurrence

def first_occurrence(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            answer = mid
            right = mid - 1

        elif book_ids[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return answer


# 3. Last Occurrence

def last_occurrence(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            answer = mid
            left = mid + 1

        elif book_ids[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return answer


# 4. Count Occurrences

def count_occurrences(book_ids, target):

    first = first_occurrence(book_ids, target)
    last = last_occurrence(book_ids, target)

    if first == -1:
        return 0

    return last - first + 1


# 5. Search Insert Position

def search_insert_position(book_ids, target):

    left = 0
    right = len(book_ids) - 1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            return mid

        elif book_ids[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return left


# 6. Floor in Sorted Array

def floor_element(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            return book_ids[mid]

        elif book_ids[mid] < target:
            answer = book_ids[mid]
            left = mid + 1

        else:
            right = mid - 1

    return answer


# 7. Ceil in Sorted Array

def ceil_element(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] == target:
            return book_ids[mid]

        elif book_ids[mid] > target:
            answer = book_ids[mid]
            right = mid - 1

        else:
            left = mid + 1

    return answer


# 8. Lower Bound

def lower_bound(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = len(book_ids)

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] >= target:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer


# 9. Upper Bound

def upper_bound(book_ids, target):

    left = 0
    right = len(book_ids) - 1
    answer = len(book_ids)

    while left <= right:

        mid = (left + right) // 2

        if book_ids[mid] > target:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer


def main():

    book_ids = [10, 20, 20, 20, 30, 40, 50]
    target = 20

    print("Binary Search       :", binary_search(book_ids, target))
    print("First Occurrence    :", first_occurrence(book_ids, target))
    print("Last Occurrence     :", last_occurrence(book_ids, target))
    print("Count Occurrences   :", count_occurrences(book_ids, target))
    print("Search Insert Pos   :", search_insert_position(book_ids, 25))
    print("Floor               :", floor_element(book_ids, 25))
    print("Ceil                :", ceil_element(book_ids, 25))
    print("Lower Bound Index   :", lower_bound(book_ids, 25))
    print("Upper Bound Index   :", upper_bound(book_ids, 20))


if __name__ == "__main__":
    main()