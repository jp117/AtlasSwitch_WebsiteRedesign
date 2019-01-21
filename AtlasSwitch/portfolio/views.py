from flask import render_template, Blueprint
from datetime import datetime


portfolio = Blueprint('portfolio', __name__)


@portfolio.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


#@portfolio.route('/portfolio', methods=['GET', 'POST'])
def portfolio_page():
    return render_template('static_site/portfolio.html')
