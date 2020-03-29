import os
import requests


# file processing
def fileProcess(url, root=None):
    if root is None:
        root = 'E://pics//'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            return path
    except Exception:
        print('sth wrong with fileProcess')


# get Response from HTML
def hunt(url, operation=None, concat_str=None, save_root=None, return_content=None, **kv):
    try:
        if operation == 'setUserAgent':
            r = requests.get(url, headers=kv)
        elif operation == 'setKeyValue':
            r = requests.get(url, params=kv)
        elif operation == 'setConcat':
            r = requests.get(url + concat_str)
        elif operation == 'setSave':
            if save_root is not None:
                path = fileProcess(url, save_root)
            else:
                path = fileProcess(url)
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        else:
            r = requests.get(url, timeout=30)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.request.url, len(r.text))
        if return_content == 'head':
            return r.text[:1000]
        elif return_content == 'tail':
            return r.text[-500:]
        else:
            return r.text
    except Exception:
        return 'sth wrong with requests'


if __name__ == '__main__':
    url1 = 'http://www.baidu.com'
    url2 = 'http://item.jd.com/2967929.html'
    url3 = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
    url4 = 'http://www.baidu.com/s'
    url5 = 'http://www.so.com/s'
    url6 = 'http://m.ip138.com/ip.asp?ip='
    url7 = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2140013030,314739014&fm=26&gp=0.jpg'

    # print(hunt(url1))
    # print(hunt(url2))
    # hunt(url3, operation='setUserAgent', kv={'user-agent': 'Mozilla/5.0'})
    # hunt(url4, operation='setParams', kv={'wd': 'abc'})
    # hunt(url5, operation='setParams', kv={'q': 'abc'})
    # hunt(url6, operation='setConcat', concat_str='192.168.1.1', return_content='tail')
    # hunt(url7, operation='setSave', save_root='/')

