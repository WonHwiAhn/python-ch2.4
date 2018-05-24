# if ~ else

a = 10

if a > 5:
    print('big')
else:
    print('small')

if a > 5:
    print('big')
else:
    pass

# if ~ elif ~ else
n = -2

if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')

order = 'spam'

if order == 'spam':
    price = 100;
elif order == 'egg':
    price = 500;
elif order == 'spagetti':
    price = 2000

print(price)

# condition Expression (tenary operator, 삼항 연산자)
# in JAVA, s = a > 5 ? 'big' : 'small'
print('# condition Expression')
print('big' if a > 5 else 'small')