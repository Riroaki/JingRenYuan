import os
import re


def cut_right(content: str, pat: str) -> str:
    """Remove right part from index of regex pattern start in content."""
    idx = content.rfind(pat)
    if idx > 0:
        content = content[:idx]
    return content


def cut_left(content: str, pat: str) -> str:
    """Remove left part of content that ends with regex pattern."""
    idx = content.find(pat)
    if idx > 0:
        content = content[idx + len(pat):]
    return content


def main():
    file_list = os.listdir('data')
    title_pat = '<title>(.*?)<'
    for file in file_list:
        if file.endswith('.html'):
            with open('data/' + file, 'r') as f:
                raw = f.read().lower()
            title = re.search(title_pat, raw).group(1)
            title = title[: title.find('_')]
            raw = cut_right(cut_left(raw, 'xiumi'), 'xiumi')
            raw = cut_left(raw, 'init();')
            raw = cut_right(raw, '推荐阅读')
            raw = cut_right(raw, '·end·')
            raw = cut_right(raw, '往期档案')
            raw = cut_right(raw, '责任编辑')
            raw = re.sub('<.*?>|[\s]+', 'RIROAKI', raw)
            lines = raw.split('RIROAKI')
            lines = list(filter(None, lines))
            with open('parsed/{}.txt'.format(title), 'w') as f:
                f.write('\n'.join(lines))
            print(title, '\tparsed.')


if __name__ == '__main__':
    main()
