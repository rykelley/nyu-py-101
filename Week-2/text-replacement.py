# i'm 100% sure i missed the point of this problem

search_text = input(str("What is the text needing replacement?:"))      # first input string
replacement_text = input(str("What is the replacement text?:"))         # second input string

num_count_1 = search_text.count(search_text)        # storing the search text to be counted
num_count_2 = replacement_text.count(replacement_text)          # storing replacement text to be counted

num_count_3 = num_count_1 + num_count_2

replaced = search_text.replace(search_text, replacement_text)       # use the replace function to swap the  strings


print(replaced)         # this is where it goes downhill i think
print(num_count_3)
