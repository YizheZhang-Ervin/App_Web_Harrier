import re
import bs4


# use regex (grid/table)
def regex_filter(html_txt=None, split=None, num=None, regex=None):
    try:
        t_list = [[] for _ in range(len(regex))]
        # column
        for i in range(len(regex)):
            t_list[i] = re.findall(regex[i], html_txt)

        o_list = [[] for _ in range(len(t_list[0]))]
        # row
        for j in range(len(t_list[0])):
            for k in range(len(t_list)):
                if split is not None and num is not None:
                    o_list[j].append(t_list[k][j].split(split)[num])
                else:
                    o_list[j].append(t_list[k][j])
        return o_list
    except Exception:
        return 'sth wrong with regex filter'


# use bs4 (grid/table)
def bs4_filter(tag, subtag, html_txt, parser):
    try:
        soup = bs4.BeautifulSoup(html_txt, parser)
        out_list = []
        for t in soup.find(tag).children:
            if isinstance(t, bs4.element.Tag):
                subt = t(subtag)
                for s in subt:
                    out_list.append(s.string)
        return out_list
    except Exception:
        return 'sth wrong with bs4 filter'


if __name__ == '__main__':
    html_txt = '<p><h1><b>123</b><h1></p>'
    tag = 'p'
    subtag = 'b'
    parser = 'html.parser'
    split = None
    num = None
    regex = [r'<p>+']
    print(regex_filter(html_txt, split, num, regex))
    print(bs4_filter(tag, subtag, html_txt, parser))
