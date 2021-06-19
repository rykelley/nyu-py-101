# 10.30:  Featured module:  requests.

# (Note:  if not using Anaconda Python, bs4 must be installed
# separately.)

import requests
import bs4

response = requests.get('http://www.nytimes.com')

page = bs4.BeautifulSoup(response.text, 'html.parser')

print(page.title)

