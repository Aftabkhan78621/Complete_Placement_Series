#  create a stack

stack = []
a =stack.append(10)
b =stack.append(20)
c =stack.append(40)

print(stack)

# for i in range(len(stack)-1, -1,-1):
#     print(stack[i])


# serch a eleemtn
found_element = 30
if found_element in stack:
    print (f'element found {stack}')

else:
    print("not found")