from flask import render_template, Blueprint


portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/portfolio', methods=['GET', 'POST'])
def portfolio_page():
    return render_template('static_site/portfolio.html')
