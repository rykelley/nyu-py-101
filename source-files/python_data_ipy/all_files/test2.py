import sys

sort_list = ['ascending', 'descending']

fh = open('FF_data.txt')

mkt_value_dict = {}

for line in fh:
    split_line = line.split()
    if split_line[0][0:4] in mkt_value_dict:
        mkt_value_dict[split_line[0][0:4]] = mkt_value_dict[split_line[0][0:4]] + float(split_line[1])
    else:
        mkt_value_dict[split_line[0][0:4]] = float(split_line[1])

try:
    user_input_1 = int(sys.argv[1])
    user_input_2 = sys.argv[2]
except IndexError:
    exit('You Did Not Enter A Result Number AND A Sort Order')
except ValueError:
    exit('You Did Not Enter A Valid Result Number')
else:
    if not user_input_1 <= len(mkt_value_dict):
        exit('Your Order Value Must Be Less Than Or Equal to {}'.format(len(mkt_value_dict)))
    if not user_input_1 > 0:
        exit('Your Order Value Must Be Greater Than Zero')
    if not sys.argv[2] in sort_list:
        exit('That is Not A Valid Sort Order')

if user_input_2 == sort_list[0]:
    sorted_mkt_value_dict = sorted(mkt_value_dict, key=mkt_value_dict.get, reverse=False)
else:
    sorted_mkt_value_dict = sorted(mkt_value_dict, key=mkt_value_dict.get, reverse=True)

for value in sorted_mkt_value_dict[:user_input_1]:
     print(value, round(mkt_value_dict[value],2))


