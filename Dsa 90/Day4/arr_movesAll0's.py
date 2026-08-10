#  1 0 2 0 3 4 0 5
#  1 2 3 4 5 0 0 0

#  two pointer approach


arr = [1,0,2,0,3,4,0,5]
print(len(arr))

write = 0
for read in range(len(arr)):
    if arr[read]  != 0:
        arr[write] , arr[read] = arr[read], arr[write]
        write += 1
print(arr)




#  MOves all -ve numbers to the end
arr = [1,-30,2,-3,3,4,-9,5]
print(len(arr))

write = 0
for read in range(len(arr)):
    if arr[read]  >= 0:
        arr[write] , arr[read] = arr[read], arr[write]
        write += 1
print(arr)


#  MOves all even numbers first
arr = [1,30,2,3,3,4,9,5]
write = 0
for read in range(len(arr)):
    if arr[read] % 2 == 0:
        arr[write], arr[read] = arr[read], arr[write]
        write += 1
print('even first: ',arr)



#  MOves all vowels
arr = ['b' ,'a', 'c','e' ,'d' ,'i' ,'o']
vowels = 'aeiouAEIOU'
write = 0
for read in range(len(arr)):
    if arr[read] in vowels:
        arr[write], arr[read] = arr[read], arr[write]
        write += 1
print('vowels: ',arr)





# for i in range(8):
#     print(i)

#  moves all 0 to front
arr = [1,0,2,0,3,4,0,5]
print(len(arr))

write = 0
for read in range(len(arr)):
    if arr[read]  == 0:
        arr[write] , arr[read] = arr[read], arr[write]
        write += 1
print(arr)




# Moves Zeros End = arr[read] != 0
# -ve end = arr[read] >=0
# even first = arr[read] % 2 == 0
# vowel first = arr[read] in vowels
# zeros front = arr[read] == 0