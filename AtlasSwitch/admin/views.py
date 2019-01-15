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


@admin.route('/admin/report_panel')
@login_required
@admin_required
def report_panel():
    return render_template('admin/report_panel.html')


@admin.route('/admin/user_panel')
@login_required
@admin_required
def user_panel():
    return render_template('admin/user_panel.html')


@admin.route('/admin/portfolio_panel')
@login_required
@admin_required
def portfolio_panel():
    return render_template('admin/portfolio_panel.html')


@admin.route('/admin/blog_panel')
@login_required
@admin_required
def blog_panel():
    return render_template('admin/blog_panel.html')


@admin.route('/admin/static_panel')
@login_required
@admin_required
def static_panel():
    return render_template('admin/static_panel.html')
