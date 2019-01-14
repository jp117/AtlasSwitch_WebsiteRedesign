from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from AtlasSwitch.users.roles import admin_required


admin = Blueprint('admin', __name__)


@admin.route('/admin')
@login_required
@admin_required
def admin_index():
    return render_template('admin/index.html')
