import requests


# get Response from HTML
def hunt(url, x=None, concat_str=None, return_content=None):
    try:
        if not str(url).startswith('http'):
            url = 'http://' + url
        if concat_str is None and x is not None:
            r = requests.get(url, x)
        elif concat_str is not None and x is None:
            r = requests.get(url+concat_str)
        elif concat_str is not None and x is not None:
            r = requests.get(url+concat_str, x)
        else:
            r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        if return_content == 'header':
            return r.headers
        elif return_content == 'text':
            return r.text
        elif return_content == 'content':
            return r.content
        else:
            return r.text
    except Exception:
        return 'sth wrong with requests'


if __name__ == '__main__':
    url1 = 'http://item.jd.com/2967929.html'
    url2 = 'http://www.so.com/s'
    url3 = 'https://www.baidu'

    # r1 = hunt(url1, return_content='head')
    # r2 = hunt(url2, x="params={'q':'xxx'}")
    # r3 = hunt(url3, concat_str='.com')
    # print(r1, r2, r3)
