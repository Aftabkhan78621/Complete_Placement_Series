# # # firt non repeating ch othrwise -1

# # def firstnonrepeating(text):
# #     freq = {}

# #     # count freq
# #     for ch in text:
# #         freq[ch] = freq.get(ch,0) + 1
    
# #     # find repeating ch
# #     for ch in text:
# #         if freq[ch] == 1:
# #             return ch
# #     return -1


# # def main():
# #     text= input("Enter a text:")
# #     result = firstnonrepeating(text)

# #     print("Answer is : ",result)

# # if __name__ == '__main__':
# #     main()


# # linear search
# def LinearSearch(arr,target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             a = ('index is : ',index)
#             b = ('index value is: ' ,arr[index])
#             return [a,b]
#     return -1
    


# def main():
#     arr = [1,20,40,50]
#     target = 40
#     result = LinearSearch(arr,target)

#     print("Answer is : ",result)

# if __name__ == '__main__':
#     main()


#  prefix sum
# def prefix_S(arr):
   
#     prefix = [0] * len(arr)

#     prefix[0] = arr[0]

#     for i in range(1,len(arr)):
#         prefix[i] = prefix[i-1] + arr[i]
#     return prefix

# def range_Sum(prefix,left,right):
#     if left == 0:
#         return prefix[right]
#     return prefix[right] - prefix[left -1]

# def main():
#     arr = [1,2,3,4,5] 
#     prefix = prefix_S(arr)

#     left = 1
#     right = 3

#     print("Sum = ",range_Sum(prefix,left,right))

# if __name__ == "__main__":
#     main()


# # remove dupicates nad count vduplicate value
# def remove_duplicate(orders):
#     if not orders:
#         return 0,[]
    
#     write = 0
#     for read in range(1,len(orders)):
#         if orders[read] != orders[write]:
#             write += 1
#             orders[write] = orders[read]
#     return write + 1 , orders[:write + 1]

# def main():
#     orders = [1,1,1,1,2,3,3,3,4,4,5,6]
#     unique_count, unique_order = remove_duplicate(orders)

#     print("uniqeCount is: ",unique_count)
#     print("uniqeorder is: ",unique_order)


# plidrome
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left +=1
        right -=1
    return True

def main():
    text= input("Enter a text: ")
    if is_palindrome(text):
        print('palindrome')
    else:
        print("Not Palindrome")

if __name__ == '__main__':
    main()
