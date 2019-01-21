from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from AtlasSwitch.users.roles import admin_required, sales_required, engineer_required


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


@employees.route('/engineering')
@login_required
@engineer_required
def engineering():
    return render_template('employee_site/engineering')
