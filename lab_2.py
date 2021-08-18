# IST-21
def merge_sort_inversions(array):
    all_values = array
    if len(all_values) == 1:
        return all_values, 0
    else:
        half_len = len(all_values) // 2
        left = all_values[:half_len]
        # print(L)
        right = all_values[half_len:]
        # print(R)
        left, left_inversions = merge_sort_inversions(left)
        right, right_inversions = merge_sort_inversions(right)
        combine_result = []
        i = 0
        j = 0
        inversions = 0 + left_inversions + right_inversions
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combine_result.append(left[i])
            i += 1
        else:
            combine_result.append(right[j])
            j += 1
            inversions += (len(left) - i)
    combine_result += left[i:]
    combine_result += right[j:]
    return combine_result, inversions


##_______________________________________
##(Користувач Аліса та Богдан)
arr1 = [1, 2, 3, 4, 5]  # Аліса
arr = [5, 2, 4, 3, 1]  # Богдан
# arr= arr1 + arr2

res = merge_sort_inversions(arr)
print(res, 'Користувач Аліса та Богдан ---', res[1], end='\n\n')

##_______________________________________
##Саме завдання 1 (Користувач 100 та 452)
arr1 = [1, 2, 3, 4, 5]  # 100     #arr1= [5, 3, 2, 1, 4]
arr = [3, 4, 5, 2, 1]  # 452     #arr2= [1, 5, 4, 3, 2]
# arr= arr1 + arr2

res = merge_sort_inversions(arr)
print(res, 'Користувач 100 та 452 ---', res[1], end='\n\n')

##_______________________________________
##Саме завдання 1 (Користувач 863 та 29)
arr1 = [1, 2, 3, 4, 5]  # 863     #arr1= [3, 1, 2, 4, 5]
arr = [1, 2, 3, 4, 5]  # 29      #arr2= [3, 1, 2, 4, 5]
# arr= arr1 + arr2

res = merge_sort_inversions(arr)
merge_sort_inversions(arr)
print(res, 'Користувач 863 та 29 ---', res[1], end='\n\n')

##_______________________________________
##Саме завдання 2 (Користувач 618 та 1)
user618 = '93 63 62 5 88 58 27 18 97 10 31 96 42 7 50 44 59 4 72 66 79 91 57 36 35 29 3 34 73 16 21 24 49 20 68 61 98 6 80 52 74 14 38 53 12 81 87 92 45 82 64 19 75 77 28 23 76 94 60 69 100 83 48 32 22 51 85 46 33 1 71 89 78 15 2 11 55 39 41 37 95 99 54 30 8 65 13 67 25 43 90 84 9 47 56 17 26 40 70 86'
user681 = user618.split(' ')
U681 = []
for i in user681:  # str to int
    U681.append(int(i))

user1 = '38 17 60 10 78 79 85 75 99 81 71 7 3 32 39 34 91 55 37 22 27 44 23 15 25 73 33 6 94 5 54 26 70 13 20 14 74 61 42 90 4 97 35 72 1 76 12 21 30 31 98 89 63 92 24 40 87 53 50 100 59 16 52 2 62 56 64 41 28 86 57 82 68 36 69 96 11 84 67 77 29 47 9 46 65 95 48 93 18 45 88 19 58 43 51 8 66 80 83 49'
user1 = user1.split(' ')
U1 = []  # str to int
for i in user1:
    U1.append(int(i))

USER681 = merge_sort_inversions(U681)[0]

###user681= '15 59 90 44 67 61 63 14 8  80 22 88 97 93 1  99 91 71 24 69 46 76 17 18 20 77 21 48 13 3 30 66 37 100 35 25 38 68 5  94 82 47 49 96 42 75 58 74 50 28 7  81 34 33 4  83 9  43 19 73  55 29 40 79 52 23 16 78 10 60 6  64 85 89 32 26 2  41 54 27 92 31 65 57 11 39 53 36 87 70 72 62 45 56 51 12 98 86 84 95'
###user1=   '38 17 60 10 78 79 85 75 99 81 71 7  3  32 39 34 91 55 37 22 27 44 23 15 25 73 33 6  94 5 54 26 70 13  20 14 74 61 42 90 4  97 35 72 1  76 12 21 30 31 98 89 63 92 24 40 87 53 50 100 59 16 52 2  62 56 64 41 28 86 57 82 68 36 69 96 11 84 67 77 29 47 9  46 65 95 48 93 18 45 88 19 58 43 51 8  66 80 83 49'
# print(USER681, U681, U1, sep='\n\n', end='\n\n')
# print(len(user681), len(user1))     #має бути 100 100

qw = {}
qwe = -1
for i in U681:
    qwe += 1
    qw[i] = U1[qwe]

USERS = {}
for i in sorted(qw.keys()):
    USERS[i] = qw[i]

USER1 = []
for i in USERS:
    USER1.append(USERS[i])

arr1 = USER681  # 681     #arr1= []
arr = USER1  # 1      #arr2= []
# arr= arr1 + arr2

res = merge_sort_inversions(arr)
print(res, 'Користувач 618 та 1 ---', res[1], end='\n\n')

##_______________________________________
##Саме завдання 2 (Користувач 951 та 178)
user951 = '78 96 1 7 22 80 81 30 40 52 8 45 31 17 65 55 76 33 88 75 50 37 32 34 5 60 26 43 92 41 57 63 44 67 54 47 12 53 77 87 83 13 49 79 35 66 99 74 72 70 15 39 28 73 84 95 24 71 97 9 19 94 36 48 62 3 86 21 10 64 82 98 38 18 20 91 16 42 2 68 59 29 27 100 85 14 90 56 89 25 46 58 69 51 23 93 61 4 11 6'
user681 = user951.split(' ')
U681 = []
for i in user681:  # str to int
    U681.append(int(i))

user178 = '92 3 36 84 51 7 100 10 69 2 23 27 68 19 1 42 59 57 39 55 89 9 11 88 85 86 31 47 12 28 16 24 41 71 44 91 5 29 37 94 4 87 25 76 49 30 6 72 22 46 79 15 35 56 67 62 73 97 13 77 93 80 60 96 48 14 66 20 32 74 54 8 78 52 83 45 75 17 34 98 95 63 58 38 61 18 53 33 90 43 82 81 99 26 64 40 70 65 21 50'
user1 = user178.split(' ')
U1 = []  # str to int
for i in user1:
    U1.append(int(i))

USER681 = merge_sort_inversions(U681)[0]

###user681= '15 59 90 44 67 61 63 14 8  80 22 88 97 93 1  99 91 71 24 69 46 76 17 18 20 77 21 48 13 3 30 66 37 100 35 25 38 68 5  94 82 47 49 96 42 75 58 74 50 28 7  81 34 33 4  83 9  43 19 73  55 29 40 79 52 23 16 78 10 60 6  64 85 89 32 26 2  41 54 27 92 31 65 57 11 39 53 36 87 70 72 62 45 56 51 12 98 86 84 95'
###user1=   '38 17 60 10 78 79 85 75 99 81 71 7  3  32 39 34 91 55 37 22 27 44 23 15 25 73 33 6  94 5 54 26 70 13  20 14 74 61 42 90 4  97 35 72 1  76 12 21 30 31 98 89 63 92 24 40 87 53 50 100 59 16 52 2  62 56 64 41 28 86 57 82 68 36 69 96 11 84 67 77 29 47 9  46 65 95 48 93 18 45 88 19 58 43 51 8  66 80 83 49'
# print(USER681, U681, U1, sep='\n\n', end='\n\n')
# print(len(user681), len(user1))     #має бути 100 100

qw = {}
qwe = -1
for i in U681:
    qwe += 1
    qw[i] = U1[qwe]

USERS = {}
for i in sorted(qw.keys()):
    USERS[i] = qw[i]

USER1 = []
for i in USERS:
    USER1.append(USERS[i])

arr1 = USER681  # 681     #arr1= []
arr = USER1  # 1      #arr2= []
# arr= arr1 + arr2

res = merge_sort_inversions(arr)
print(res, 'Користувач 951 та 178 ---', res[1], end='\n\n')
input()
