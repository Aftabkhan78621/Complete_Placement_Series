# # Question

# Given a sorted array of Order IDs, remove duplicates in-place and return:
# • Number of unique Order IDs.
# • Unique Order IDs.

# Conditions:
# • Don't use set().
# • Don't create another array.
# • Modify the same array (In-place).

# Example:

# Input:
# orders = [1,1,2,2,3,4,4,5]

# Output:
# Unique Count = 5
# Unique Orders = [1,2,3,4,5]

# # Answer (Approach)

# • Since the array is sorted, duplicate elements are adjacent.
# • Use Two Pointers:
#   - write → Position to place the next unique element.
#   - read → Traverses the array.
# • Copy every new unique element to the write position.
# • Return write + 1 as the unique count.

# # Algorithm

# 1. If the array is empty, return 0.
# 2. Initialize write = 0.
# 3. Traverse using read from index 1.
# 4. If orders[read] != orders[write]:
#    • Increment write.
#    • Copy current element to orders[write].
# 5. Return:
#    • Unique Count = write + 1
#    • Unique Orders = orders[:write + 1]

# # Python Code

# def remove_duplicates(orders):

#     if not orders:
#         return 0, []

#     write = 0

#     for read in range(1, len(orders)):
#         if orders[read] != orders[write]:
#             write += 1
#             orders[write] = orders[read]

#     return write + 1, orders[:write + 1]

# # Short Explanation

# • Sorted array me duplicates hamesha consecutive hote hain.
# • read pointer poora array scan karta hai.
# • write pointer next unique element ki position batata hai.
# • Har unique element ko same array me copy kiya jata hai.
# • Last me write + 1 unique elements ki total count hoti hai.

# ### Important Code Lines

# if not orders:
# • Empty array ko handle karta hai.
# write = 0
# • Pehla element hamesha unique hota hai.
# for read in range(1, len(orders)):
# • Second element se comparison start hota hai.
# if orders[read] != orders[write]:
# • Check karta hai ki naya unique element mila ya nahi.
# write += 1

# • Next unique position par move karta hai.
# orders[write] = orders[read]
# • Unique element ko uski correct position par copy karta hai.
# return write + 1, orders[:write + 1]

# • Unique count aur unique elements return karta hai.

# # Important Points
# • Array sorted hona zaroori hai.
# • No extra array is used.
# • In-place modification hoti hai.
# • write final unique index ko represent karta hai.
# • Unique Count = write + 1.

# # Edge Cases:

# Input: []
# Output:
# Count = 0

# Input: [1]
# Output:
# Count = 1

# Input: [1,1,1,1]
# Output:
# Count = 1

# Input: [1,2,3,4]
# Output:
# Count = 4

# # Time Complexity
# O(n)
# # Space Complexity
# O(1)

# # Similar Questions

# • LeetCode 26 – Remove Duplicates from Sorted Array
# • LeetCode 80 – Remove Duplicates from Sorted Array II
# • LeetCode 27 – Remove Element
# • LeetCode 283 – Move Zeroes
# • LeetCode 88 – Merge Sorted Array
# • LeetCode 167 – Two Sum II

# # Follow-up Questions
# • Return only the unique count.
# • Keep each duplicate at most twice.
# • Remove a given value instead of duplicates.
# • Remove duplicates from an unsorted array.
# • Move duplicates to the end.

# # Pattern Recognition
# Keywords:
# • Sorted Array
# • Remove Duplicates
# • In-place
# • Constant Space
# • Return New Length

# ➡️ Think Two Pointer Technique.


def remove_duplicates(orders):
    if not orders:
        return 0,[]
    
    write = 0
    for read in range(1,len(orders)):
        if orders[read] != orders[write]:
            write += 1
            orders[write] = orders[read]
    return write +1 ,orders[:write + 1]




def main():
    orders = [1,1,1,2,3,3,4,5,5,5,6]
    unique_count , unique_order = remove_duplicates(orders)
    print("unique_Count: ",unique_count)
    print("unique_order: ",unique_order)


if __name__ == '__main__':
    main()