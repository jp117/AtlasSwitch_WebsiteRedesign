from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required


users = Blueprint('users', __name__)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('employees.index')
            return redirect(next)
        else:
            error = 'Invalid email or password'
        # if a user was trying to access a page that required a log in, this will let them go to that page after log in

    return render_template('static_site/login.html', form=form, error=error)
