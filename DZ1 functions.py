# дз1. Функция sum_range
def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s

a, b = map(int, input().split())
print(sum_range(a, b))

# дз2. Преобразование списка во множество
my_list = [1, 'list', 2, 3, 1, 0, 4, 3, 1, 4, 'list']
my_set = set(my_list)
print(my_set)














