str_length = input('please type length:')
str_width = input('please type width:')

total_price = input('How much for 1 meter?')

str_length =float(str_length)
str_width =float(str_width)
total_price = float(total_price)

area = str_length * str_width

total_price = area * total_price

area = str(area)
total_price = str(total_price)
print('the total area is'+area)
print('give the guy $'+total_price)