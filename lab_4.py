# IST-21

# Кодування букв в числа
alpha_to_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}


def counting_sort(all_values):
    k = max(all_values)
    clear_list = [0] * 27  # 26 літер + 1
    list_of_values = [None] * len(all_values)  # для результату
    print(' C  =', clear_list, '\n max (k)=', k, '\n B=', list_of_values)

    print(range(len(all_values)))
    for i in range(len(all_values)):
        print(' i=', i)
        clear_list[all_values[i][0]] += 1
        print(clear_list)
    # print(" C' =", C)

    for j in range(1, 27):  # не включати C[0] елемент!
        # print(' j=', j)
        clear_list[j] = clear_list[j] + clear_list[j - 1]
        # print(C)
    # print(" C''=", C)

    i = len(all_values)
    for lorem in range(len(all_values)):
        i = i - 1
        # print(' i=', i)

        list_of_values[clear_list[all_values[i][0]] - 1] = all_values[i]
        clear_list[all_values[i][0]] = clear_list[all_values[i][0]] - 1
        # print('B=', B, '\nC=', C)

    return all_values, clear_list, list_of_values


def radix_sort(all_values, d):
    for i in range(d):
        print('_' * 10, 'Radix:', i, '_' * 10)
        r = counting_sort(all_values)[2]
        print(r)
    return r


AA = ['hzt', 'sng', 'ena', 'sdt', 'qds', 'yif', 'slt', 'lpz', 'cqc', 'hpo']
d = len(max(AA))

# Кодування букв. Тобто "acb" буде [1,3,2]
A = []
for i in AA:
    A.append([alpha_to_number[i[0]], alpha_to_number[i[1]], alpha_to_number[i[2]]])

print('=' * 50)
print(A, end='\n\n')

# Z= CountingSort(A)
Z = radix_sort(A, d)

print('Sorted:', Z)
print('=' * 50)
