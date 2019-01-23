from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User, FollowUp
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from AtlasSwitch.users.roles import admin_required, sales_required, engineer_required
from AtlasSwitch.quote.forms import NewQuote
import datetime
from AtlasSwitch import db


employees = Blueprint('employees', __name__)


@employees.route('/employees')
@login_required
def index():
    return render_template('employee_site/index.html')


@employees.route('/sales')
@login_required
@sales_required
def sales():
    return render_template('employee_site/sales.html')


@employees.route('/sales/quote', methods=['GET', 'POST'])
@login_required
@sales_required
def quote():
    newquote = NewQuote()
    if newquote.validate_on_submit():
        newquoteentry = FollowUp(salesman=current_user.name,
                                 jobname=newquote.jobname.data,
                                 job_address=newquote.jobaddress.data,
                                 amount=newquote.amount.data,
                                 date=datetime.date.today(),
                                 nextfollowup=newquote.followdate.data,
                                 notes=newquote.notes.data)
        db.session.add(newquoteentry)
        db.session.commit()
        return redirect(url_for('employees.quote'))
    return render_template('employee_site/quote.html', newquote=newquote)


@employees.route('/quote/all_quotes')
@login_required
@sales_required
def all_quotes():
    page = request.args.get('page', 1, type=int)
    quotes = FollowUp.query.order_by(FollowUp.id.desc()).paginate(page=page, per_page=100)
    return render_template('employee_site/all_quotes.html', quotes=quotes)


@employees.route('/sales/crm')
@login_required
@sales_required
def crm():
    return render_template('employee_site/crm.html')


@employees.route('/engineering')
@login_required
@engineer_required
def engineering():
    return render_template('employee_site/engineering.html')


@employees.route('/advisory_board')
@login_required
def advisory_board():
    return render_template('employee_site/advisory_board.html')
