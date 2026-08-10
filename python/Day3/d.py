# x = 'Awesome'

# def fun():
#     print("x is "+ x)
# fun()

x = 'awesome'

def fun():
    x = 'fantastic'
    print('python is '+x)
fun()

print('python is '+x)

x = 'fanta'
def func():
    global x
    x = 'global var'
func()
print('python is '+ x)