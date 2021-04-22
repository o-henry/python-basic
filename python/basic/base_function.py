def add(a, b):
    return a+b


print(add(3, 5))

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


# 람다
# argument, logic, parameter
print((lambda a, b: a+b)(6, 7))
