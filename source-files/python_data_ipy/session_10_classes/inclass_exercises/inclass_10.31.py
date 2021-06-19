# 10.31:  Featured module:  re.

import re

line = 'a phone number:  213-298-1990'

matchobj = re.search(r'(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)', line)

print(matchobj.group(1))

