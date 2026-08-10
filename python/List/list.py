# # thislist = ["apple", "banana", "cherry"]
# # print(thislist)

# # thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# # print(thislist)

# # list1 = ["apple", "banana", "cherry"]
# # list2 = [1, 5, 7, 9, 3]
# # list3 = [True, False, False]
# # print(list1,list2,list3)

# # list1 = ["abc", 34, True, 40, "male"]
# # print(list1)

# # thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[-1])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[:4])


# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[2:5])

# # thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # print(thislist[-4:-1])
# # if 'apple' in thislist:
# #   print("Yes, 'apple' is in the fruits list")

# #   thislist = ["apple", "banana", "cherry"]
# # thislist[1] = "blackcurrant"
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist[1:2] = ["blackcurrant", "watermelon"]
# # print(thislist)

# # thislist.insert(2,'watermelon')
# # print(thislist)



# # thislist = ["apple", "banana", "cherry"]
# # tropical = ["mango", "pineapple", "papaya"]
# # thislist.extend(tropical)
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist.remove("banana")
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist.pop(1)
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # thislist.pop()
# # print(thislist)

# # thislist = ["apple", "banana", "cherry"]
# # del thislist[0]
# # print(thislist)

# thislist = ["apple", "banana", "cherry"]
# # thislist.clear()
# # print(thislist)

# # for x in thislist:
# #     print(x)

# # for i in range(len(thislist)):
# #     print(thislist[i])

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1
# [print(x) for x in thislist ]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if 'a' in x]
print(newlist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)















