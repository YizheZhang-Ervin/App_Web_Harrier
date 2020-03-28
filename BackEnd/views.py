from flask import Blueprint, request, render_template


hunter = Blueprint('hunter', __name__)


def init_blue(app):
    app.register_blueprint(hunter)


# index.html
@hunter.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


# error handler
@hunter.errorhandler(404)
def page_not_found(error):
    # use template
    return render_template('404.html'), 404
    # gain response and change
    # resp = make_response(render_template('404.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp
