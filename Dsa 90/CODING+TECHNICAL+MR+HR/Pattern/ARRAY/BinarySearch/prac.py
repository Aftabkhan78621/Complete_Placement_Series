# def binaryS(a,t):
#     l = 0
#     r= len(a) - 1
#     while l <= r:
#         mid = l + (r-l) // 2
#         if a[mid] == t:
#             return mid
#         elif a[mid] <t:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return -1
# print(binaryS([1,2,3,4,5], 3))

# def binarySFO(a,t):
#     l = 0
#     r= len(a) - 1
#     ans = -1
#     while l <= r:
#         mid = l + (r-l) // 2
#         if a[mid] == t:
#             ans = mid
#             r = mid - 1
#         elif a[mid] <t:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return ans
# print(binarySFO([1,3,3,4,5], 3))

# def binarySLO(a,t):
#     l = 0
#     r= len(a) - 1
#     ans = -1
#     while l <= r:
#         mid = l + (r-l) // 2
#         if a[mid] == t:
#             ans = mid
#             l = mid + 1
#         elif a[mid] <t:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return ans
# print(binarySLO([1,3,3,4,5], 3))

# def countOcc(a,t):
#     first = binarySFO(a,t)
#     if first == -1:
#         return 0
#     last = binarySLO(a,t)
#     return last - first + 1
# print(countOcc([1,3,3,4,5], 3))


# peak elemtn
def peakElement(a):
    l = 0 
    r = len(a) - 1
    while l <r:
        m = l +(r-l)//2
        if a[m] < a[m + 1]:
            l = m + 1
        else:
            r = m
    return l, a[l]
index,value = peakElement([1,2,3,4,5,0]) 
print("Index is: ",index)
print("value of index is: ",value)













