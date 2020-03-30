import requests


# requests
def hunt(viewpart=None, method=None, url=None, timeout=None, headers=None, params=None,
         data=None, json=None, cookies=None, files=None, proxies=None, auth=None, cert=None,
         allow_redirects=True, verify=True, stream=True, code=None):

    # data cleaning
    if viewpart is None or viewpart == '': viewpart = ''
    if method is None or method == '': method = 'GET'
    if url is None or url == '':
        url = ''
    elif not str(url).startswith('http'):
        url = 'https://' + url
    if timeout is None or timeout == '': timeout = 30
    if headers is None or headers == '': headers = {}
    if params is None or params == '': params = {}
    if data is None or data == '': data = {}
    if json is None or json == '': json = {}
    if cookies is None or cookies == '': cookies = {}
    if files is None or files == '': files = {}
    if proxies is None or proxies == '': proxies = {}
    if auth is None or auth == '': auth = ()
    if cert is None or cert == '': cert = ''
    if code is None or code == '': code = ''
    # start request
    try:
        response = requests.request(method=method, url=url, timeout=int(timeout), headers=headers, params=params, data=data,
                                    json=json, allow_redirects=allow_redirects, cookies=cookies, files=files, auth=auth,
                                    verify=verify, cert=cert, proxies=proxies, stream=stream)
        response.raise_for_status()
        if code == '':
            response.encoding = response.apparent_encoding
        else:
            response.encoding = code
        if viewpart == 'headers':
            return response.headers
        elif viewpart == 'json':
            return response.json()
        elif viewpart == 'content':
            return response.content
        else:
            return response.text
    except Exception as e:
        return 'Sth Wrong with Hunter, please change parameters and try again'
