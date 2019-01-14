from flask import render_template, Blueprint


core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('static_site/index.html')


@core.route('/history')
def history():
    return render_template('static_site/history.html')


@core.route('/team')
def team():
    # This is probably going to pull from the database
    return render_template('static_site/team.html')


@core.route('/products_and_services')
def products_and_services():
    return render_template('static_site/pands.html')


@core.route('/contact')
def contact():
    return render_template('static_site/contact.html')
