from flask import render_template, Blueprint, request
from AtlasSwitch.models import User, History, PandS
from datetime import datetime


core = Blueprint('core', __name__)


@core.context_processor
def inject_now():
    return {'now':datetime.utcnow()}


@core.route('/')
def index():
    return render_template('static_site/index.html')


@core.route('/history')
def history():
    history = History.query.get(1)
    return render_template('static_site/history.html', history=history)


@core.route('/team')
def team():
    # This is probably going to pull from the database
    return render_template('static_site/team.html')


@core.route('/products_and_services')
def products_and_services():
    page = request.args.get('page', 1, type=int)
    pands = PandS.query.order_by(PandS.id.asc()).paginate(page=page, per_page=20)
    return render_template('static_site/pands.html', pands=pands)


@core.route('/contact')
def contact():
    return render_template('static_site/contact.html')
