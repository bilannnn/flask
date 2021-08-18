# IST-21
def partition(all_values, p, r, count):
    # p - x
    # r - y
    # A[0], A[-1]= A[-1], A[0]
    print(all_values)
    position = p
    # j= p
    x = all_values[p]
    # print(' p=',p, ' r=',r, ' i=',i, ' x=',x, sep='')
    for j in range(p + 1, r + 1):
        # count= count + 1
        if all_values[j] <= x:
            position = position + 1
            all_values[position], all_values[j] = all_values[j], all_values[position]

    all_values[position], all_values[p] = all_values[p], all_values[position]
    return position, count + (r - p)


def quick_sort(all_values, p, r, count):
    if p < r:
        q, count = partition(all_values, p, r, count)
        count = quick_sort(all_values, p, q - 1, count)[1]
        count = quick_sort(all_values, q + 1, r, count)[1]
    return all_values, count


A = [6, 10, 2, 4, 1, 3, 5, 7, 9, 8]  # count має дорівнювати 20!(сортування по ПЕРШОМУ елементу)
print(A)

p = 0
r = len(A) - 1
print(quick_sort(A, p, r, 0))
input()
