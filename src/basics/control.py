'''
subject: 控制流用法

'''
# -*- coding: utf-8 -*-

print("ifelse---------------------------------------------------")

height=1.75
weight=80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

print("match---------------------------------------------------")
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


args = ['gcc', 'hello.c', 'world.c']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

print("for---------------------------------------------------")

sum = 0
# range(10) 生成了一个包含 10 个值的链表
for x in range(101):
    sum = sum + x
print(sum)


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue #  break
    print(n)



