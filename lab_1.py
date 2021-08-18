# IST-21
print('x*y=Z')


def karacuba():
    x = input('\nx:')
    y = input('y:')
    len_x = len(x)

    half_len_x = int(len(x) / 2)
    half_len_y = int(len(y) / 2)

    # x= a_b
    # x = 1234
    # a = 12
    # b = 34
    x_first_part = int(x[:half_len_x])
    x_second_part = int(x[half_len_x:])
    print(x_first_part, x_second_part, sep='_')

    # y= c_d
    y_first_part = int(y[:half_len_y])
    y_second_part = int(y[half_len_y:])
    print(y_first_part, y_second_part, sep='_')

    z_first_part = (10 ** len_x) * x_first_part * y_first_part
    z_combine_part = (x_first_part + x_second_part) * (y_first_part + y_second_part) - x_first_part * y_first_part - \
                     x_second_part * y_second_part
    z_combine = (10 ** (len_x / 2)) * z_combine_part
    z_second_part = x_second_part * y_second_part
    # Z= (10**n)*a*c + (10**(n/2))*(a*d+b*c) + b*d
    z = z_first_part + z_combine + z_second_part
    print('\nZ=', int(z))


while True:
    karacuba()
