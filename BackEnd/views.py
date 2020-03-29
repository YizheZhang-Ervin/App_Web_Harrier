from urllib import parse

from flask import Blueprint, request, render_template, abort

from Hunter.request_common import hunt

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
        if para_dict.get('engine') == 'Harrier' or para_dict.get('engine') == '':
            setKV = para_dict.get('setKV', '')
            setHeader = para_dict.get('setHeader', '')
            if setHeader != '' and setKV == '':
                x = para_dict.get('setHeader', '')
            elif setHeader == '' and setKV != '':
                x = para_dict.get('setKV', '')
            elif setHeader != '' and setKV != '':
                x = para_dict.get('setHeader', '') + ',' + para_dict.get('setKV', '')
            else:
                x = ''
            result = hunt(url=para_dict.get('url', ''), concat_str=para_dict.get('concat', ''),
                          return_content=para_dict.get('viewpart', ''), x=x)

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
