# -*- coding: utf-8 -*-

import re
import os


def change_title(file):
    print 'Processing: ', file
    patt = re.compile('<title>(.*?)</title>', re.S)
    with open('./html/' + file, 'r') as f:
        content = f.read()
    res = patt.findall(content)
    if res:
        new_title = res[0].split('\n')[0]
        # print 'new', new_title
        content = patt.sub(
            '<title>{}</title>'.format(new_title), content, count=1)
        with open('./html/' + file, 'w') as f:
            f.write(content)


if __name__ == "__main__":
    for file in os.listdir('./html'):
        if os.path.splitext(file)[1] == '.html':
            change_title(file)
