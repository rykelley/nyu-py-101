# 10.29:  Featured module: bs4.

# (Note:  if not using Anaconda Python, this module must be
# installed separately.)

import bs4

fh = open('../dormouse.html')

text = fh.read()

page = bs4.BeautifulSoup(text, 'html.parser')

print(page.title)

fh.close()

