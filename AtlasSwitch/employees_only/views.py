from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from AtlasSwitch.users.roles import admin_required


employees = Blueprint('employees', __name__)


@employees.route('/employees')
@login_required
@admin_required
def index():
    return render_template('employee_site/index.html')
