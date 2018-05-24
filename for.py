# for 반복문
print('# for 반복문')
a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print()

print('!!!!')

# 복합 자료형을 사용하는 for문
print('# 복합 자료형을 사용하는 for문')
l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]

for data in l:
    print('이름: %s, 나이: %d' % data)
else:
    pass

# format형식 - unpacking방식
print('# unpacking방식')
for name, age in l:
    print('이름: {}, 나이: {}'.format(name, age))

# format형식 - dictionary방식
l = [
        {'name': '둘리', 'age': 10},
        {'name': '마이콜', 'age': 20},
        {'name': '도우넛', 'age': 30}
    ]

print('#dictionary 방식')
for data in l:
    print('이름: %(name)s, 나이: %(age)d' % data)

# 1~10 합 구하기
print('\n# 1~10 합 구하기')
s = 0
for i in range(1, 11):
    s += i

print(s)

# break
print('\n#break')
for i in range(10):
    if i > 5:
        break;

    print(i, end=' ')

else: # break 다음에 else를 안 탐.
    print('')

print('종료')

# continue
print('\ncontinue')
for i in range(10):
    if i <= 5:
        continue
    print(i, end=' ')
else: # continue문은 else를 탐.
    print('')

print('종료')

# 구구단
a = 9
b = 9