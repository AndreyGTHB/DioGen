x, y = input().split(' ')
x = int(x)
y = int(y)
if x == 1:
    print('YES')
    exit()


houses_before = x - 1
houses_in_porch = y - x + 1
if houses_before % houses_in_porch == 0:
    print('YES')
else:
    print('NO')

