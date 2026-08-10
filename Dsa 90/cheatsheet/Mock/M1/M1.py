

# def MoveNegetive(arr):
#     l = 0
#     for r in range(1,len(arr)):
#         if arr[r] >= 0:
#             arr[r],arr[l] = arr[l],arr[r]
#             l += 1
#     return arr
# print(MoveNegetive([-10,-90,10,1,1,1]) )

# left = 0

# def subsequence(s1,s2):
#     l = 0 
#     for r in range(len(s2)):
#         if left == len(s1):
#             break
#         if s1[l] == s2[r]:
#             l += 1
#     return l == len(s1)

# print(subsequence('ace','abcde'))
# print(subsequence('aec','abcde'))

# def subsequence(s1, s2):
#     left = 0
#     for right in range(len(s2)):
#         if left == len(s1):
#             break
#         if s1[left] == s2[right]:
#             left += 1
#     return left == len(s1)


# print(subsequence("ace", "abcde"))   # True
# print(subsequence("aec", "abcde"))   # False
# print(subsequence("abc", "abc"))     # True
# print(subsequence("abcd", "abc"))    # False

# num = 1
# for i in range(5):
#     for j in range(i):
#         print(num,end=' ')
#         num += 1
#     print()

# def isAngram(s1,s2):
#     return sorted(s1) == sorted(s2)
# print(isAngram("hello",'world'))

# for i in range(5):
#     for j in range(i):
#         print(num,end='')
#         num += 1
#     print()

# num = 1
# for i in range(4):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# # reverse string
# def reverses(text):

#     words = text.split()

#     result = ""

#     for i in range(len(words) - 1, -1, -1):

#         result += words[i]

#         if i != 0:
#             result += " "

#     return result


# print(reverses("i Love coding"))

# def rev(str):
#     return ' '.join(str.split()[::-1])
# print(rev('i love coding'))


# third
f = float('-inf')  
s = float('-inf')
t = float('-inf')

a = [ 2,4,5,7,6]
for num in a:
    if num > f:
        s = f  
        f = num 
        t = s