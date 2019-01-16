from flask import render_template, Blueprint, url_for, request, redirect, flash
from AtlasSwitch.models import User, History
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from AtlasSwitch.users.roles import admin_required
from AtlasSwitch.users.forms import NewUserForm
from AtlasSwitch.admin.forms import HistoryForm
from AtlasSwitch import db


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
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.id.asc()).paginate(page=page, per_page=20)
    return render_template('admin/user_panel.html', users=users)


@admin.route('/admin/create_new_user', methods=['GET', 'POST'])
@login_required
@admin_required
def create_new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data,
                        email=form.email.data,
                        access_level=form.access_level.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin.user_panel'))
    return render_template('/admin/create_new_user.html', form=form)


@admin.route('/admin/<int:user_id>/delete', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if current_user.id != user_id:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('admin.user_panel'))
    else:
        error = 'Cannot delete yourself'
        flash(error)
    return redirect(url_for('admin.user_panel', error=error))


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


@admin.route('/admin/static_panel', methods=['GET', 'POST'])
@login_required
@admin_required
def static_panel():
    history_post = History.query.get_or_404(1)
    history = HistoryForm()
    if history.validate_on_submit():
        history_post.text = history.text.data
        db.session.commit()
        return redirect(url_for('admin.static_panel'))
    elif request.method == 'GET':
        history.text.data = history_post.text

    return render_template('admin/static_panel.html', history=history)
