'''
subject: 迭代器与生成器

https://www.cnblogs.com/derek1184405959/p/8043411.html

'''

print("迭代器---------------------------------------------------")

from collections.abc import Iterable

city = ['beijing','shanghai','tinajin','chongqin']

# 是否是可迭代对象，可迭代都可用迭代器
print(isinstance(city, Iterable))

for x in iter(city):
    print(x)

for index,item in enumerate(city):
    print(index,item)


# 字典迭代器
d = {'a': 1, 'b': 2, 'c': 3}

print(isinstance(d, Iterable))

for k in d:
    print(k,str(d[k]))

for v in d.values():
    print(v)

print("生成器---------------------------------------------------")

'''
生成器
有yield的关键字的函数为生成器函数
每次执行一次到yield的时候,函数会暂停执行,并将当前的值返回给调用者
当下一次迭代时,函数会从暂停的地方继续执行

目的：实现了按需生成数据的效果，避免了一次性生成所有数据并存储在内存中，提高了效率和节省了内存空间
'''

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()

# 继承上一次的指针
print(next(o))
print(next(o))
print(next(o))

# 指针永远返回1
print(next(odd()))
print(next(odd()))
print(next(odd()))

def generator(low,high):
    while low <= high:
        yield low
        low += 1


for i in generator(1,10):
    print(i,end='')
