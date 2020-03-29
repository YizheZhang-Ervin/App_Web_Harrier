from urllib import parse

from flask import Blueprint, request, render_template, abort

from Hunter.requests import hunt

hunter = Blueprint('hunter', __name__)


def init_blue(app):
    app.register_blueprint(hunter)


# index.html
@hunter.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result='', content='', name='')
    if request.method == 'POST':
        parameters = request.form
        para_dict = {}
        for k, v in parameters.items():
            para_dict[k] = v
        if para_dict.get('engine', '') == '':
            para_dict['engine'] = 'Harrier'
        if para_dict.get('engine', 'Harrier') == 'Harrier':
            result = hunt(viewpart=para_dict.get('viewpart', ''), method=para_dict.get('method', ''),
                          url=para_dict.get('url', ''), timeout=para_dict.get('timeout', ''),
                          header=para_dict.get('setHeader', ''), params=para_dict.get('setParams', ''),
                          data=para_dict.get('setData', ''), json=para_dict.get('setJson', ''),
                          cookies=para_dict.get('cookies', ''),  files=para_dict.get('files', ''),
                          proxies=para_dict.get('proxies', ''), auth=para_dict.get('auth', ''),
                          cert=para_dict.get('cert', ''), allow_redirects=para_dict.get('allow_redirects', ''),
                          verify=para_dict.get('verify', ''), stream=para_dict.get('stream', ''))
            content = "data:application/html;charset=utf-8," + parse.quote(result)
            name = para_dict.get('url', '').split('/')[-1]
        else:
            result = ''
            content = ''
            name = ''
        return render_template('index.html', result=result, content=content, name=name)


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
