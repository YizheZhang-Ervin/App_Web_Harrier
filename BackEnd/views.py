from urllib import parse

from flask import Blueprint, request, render_template, abort

from Hunter.filter import regex_filter, bs4_filter
from Hunter.output import output_list
from Hunter.requests import hunt

hunter = Blueprint('hunter', __name__)


def init_blue(app):
    app.register_blueprint(hunter)


# index.html
@hunter.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result='', content='', name='')


@hunter.route('/hunt', methods=['POST'])
def huntform():
    if request.method == 'POST':
        parameters = request.form
        para_dict = {}
        for k, v in parameters.items():
            para_dict[k] = v
        if para_dict.get('engine', '') == '':
            para_dict['engine'] = 'Harrier'
        if para_dict.get('engine', 'Harrier') == 'Harrier':
            result = hunt(viewpart=para_dict.get('viewpart', None), method=para_dict.get('method', None),
                          url=para_dict.get('url', None), timeout=para_dict.get('timeout', None),
                          headers=para_dict.get('setHeaders', None), params=para_dict.get('setParams', None),
                          data=para_dict.get('setData', None), json=para_dict.get('setJson', None),
                          cookies=para_dict.get('cookies', None), files=para_dict.get('files', None),
                          proxies=para_dict.get('proxies', None), auth=para_dict.get('auth', None),
                          cert=para_dict.get('cert', None), allow_redirects=para_dict.get('allow_redirects', None),
                          verify=para_dict.get('verify', None), stream=para_dict.get('stream', None),
                          code=para_dict.get('encoding', None))
            content = "data:application/html;charset=utf-8," + parse.quote(result)
            name = para_dict.get('url', '').split('/')[-1]
        else:
            result = ''
            content = ''
            name = ''
        return render_template('index.html', result=result, content=content, name=name)


@hunter.route('/filter', methods=['POST'])
def filterform():
    if request.method == 'POST':
        parameters = request.form
        para_dict = {}
        for k, v in parameters.items():
            para_dict[k] = v
        rg = para_dict.get('regex', '')
        if rg != '' and rg is not None:
            result = regex_filter(html_txt=para_dict.get('html_txt', ''), split=para_dict.get('split', ''),
                                  num=para_dict.get('num', ''), regex=rg)
        else:
            result = bs4_filter(tag=para_dict.get('tag', ''), subtag=para_dict.get('subtag', ''),
                                html_txt=para_dict.get('html_txt', ''), parser=para_dict.get('parser', ''))
        global results
        results = result
        return render_template('index.html', result=result, content='', name='')


@hunter.route('/output', methods=['POST'])
def outputform():
    if request.method == 'POST':
        parameters = request.form
        para_dict = {}
        for k, v in parameters.items():
            para_dict[k] = v
        col_name = para_dict.get('col_name', '')
        result = output_list(liss=results, output_format=para_dict.get('format', ''), col_name=col_name)
        content = "data:application/html;charset=utf-8," + parse.quote(result)
        return render_template('index.html', result=result, content=content, name="output")


# document.html
@hunter.route('/document', methods=['GET', 'POST'])
def document():
    if request.method == 'GET':
        return render_template('document.html')


# error handler
@hunter.errorhandler(404)
def page_not_found(error):
    # use template
    return render_template('404.html'), 404
    # gain response and change
    # resp = make_response(render_template('404.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp


@hunter.route('/404')
def other():
    abort(404)
