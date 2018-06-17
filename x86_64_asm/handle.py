# -*- coding: utf-8 -*-

import re
import os

global index_content


def handle(filename):
    global index_content
    print 'Processing: ', filename
    patt = re.compile('<title>(.*?)</title>', re.S)
    with open(filename, 'r') as f:
        content = f.read()
    res = patt.findall(content)
    if res:
        new_title = res[0].split('\n')[0]
        # print 'new', new_title
        content = patt.sub(
            '<title>{}</title>'.format(new_title), content, count=1)
        with open(filename, 'w') as f:
            f.write(content)

    # rename filename to be compatible with Windows
    if ':' in filename:
        new_name = filename.replace(':', '-')
        print 'old name:', filename
        print 'new name:', new_name
        os.rename(filename, new_name)
        index_content = index_content.replace(filename, new_name)


if __name__ == "__main__":
    os.chdir('./html')
    with open('./index.html', 'r') as f:
        index_content = f.read()
    for filename in os.listdir('.'):
        if os.path.splitext(filename)[1] == '.html':
            handle(filename)
    with open('./index.html', 'w') as f:
        f.write(index_content)