import requests


# requests
def hunt(viewpart=None, method=None, url=None, timeout=None, header=None, params=None, data=None, json=None,
         cookies=None, files=None, proxies=None, auth=None, cert=None, allow_redirects=True, verify=True, stream=True):

    # data cleaning
    if viewpart is None: viewpart = ''
    if method is None: method = 'GET'
    if url is None:
        url = ''
    elif not str(url).startswith('http'):
        url = 'https://' + url
    if timeout is None: timeout = 30
    if header is None: header = {}
    if params is None: params = {}
    if data is None: data = {}
    if json is None: json = {}
    if cookies is None: cookies = {}
    if files is None: files = {}
    if proxies is None: proxies = {}
    if auth is None: auth = ()
    if cert is None: cert = ''

    # start request
    try:
        response = requests.request(method=method, url=url, timeout=timeout, header=header, params=params, data=data,
                                    json=json, allow_redirects=allow_redirects, cookies=cookies, files=files, auth=auth,
                                    verify=verify, cert=cert, proxies=proxies, stream=stream)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        if viewpart == 'header':
            return response.headers
        elif viewpart == 'json':
            return response.json()
        elif viewpart == 'content':
            return response.content
        else:
            return response.text
    except Exception:
        return 'Sth Wrong with Hunter, please change parameters and try again'
