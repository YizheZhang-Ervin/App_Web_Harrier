from urllib import parse

from flask import Blueprint, request, render_template

from Hunter.request_common import hunt

hunter = Blueprint('hunter', __name__)


def init_blue(app):
    app.register_blueprint(hunter)


# index.html
@hunter.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', result='', content='')
    if request.method == 'POST':
        parameters = request.form
        para_dict = {}
        for k, v in parameters.items():
            para_dict[k] = v
        if para_dict.get('engine') == 'Harrier':
            result = hunt(url=para_dict.get('url', ''), operation=para_dict.get('operation', ''),
                          concat_str=para_dict.get('content', ''), save_root=None,
                          return_content=para_dict.get('viewpart', ''), kv=para_dict.get('keyvalue', ''))
            content = "data:application/html;charset=utf-8," + parse.quote(result)
        else:
            result = ''
            content = ''
        return render_template('index.html', result=result, content=content)


# error handler
@hunter.errorhandler(404)
def page_not_found(error):
    # use template
    return render_template('404.html'), 404
    # gain response and change
    # resp = make_response(render_template('404.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp
