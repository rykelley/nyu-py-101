var_1 = int(input('Please enter an integer:  '))
var_2 = int(input('Please enter another integer:  '))

power_of = var_1 ** var_2
power_of_str = str(power_of)
power_of_len = len(power_of_str)
border = power_of_len * '='

print(f'{border}')

print(f'Total {power_of}')
