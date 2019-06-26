from random import random
from time import sleep
from requests import get
import re

headers = {'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/74.0.3729.169 Safari/537.36')}
pat = 'question_link" href="(.*?)"'
raw = 'https://chuansongme.com/account/jingrenyuan?start='
essay_head = 'https://chuansongme.com'
url_list = ['https://chuansongme.com/account/jingrenyuan']
for i in range(1, 84):
    idx = i * 12
    url = raw + str(idx)
    url_list.append(url)
for url in url_list:
    sleep(random() * 2 + 1)
    content = get(url, headers=headers).text
    for s in re.findall(pat, content):
        name = 'data/' + s[s.rfind('/') + 1:] + '.html'
        essay_url = essay_head + s
        print(essay_url)
        sleep(random() * 2 + 1)
        with open(name, 'w') as f:
            f.write(get(essay_url, headers=headers).text)
