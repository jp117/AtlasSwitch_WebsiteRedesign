from flask import render_template, Blueprint, url_for, request, redirect
from AtlasSwitch.models import User
from AtlasSwitch.users.forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required


users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
        # if a user was trying to access a page that required a log in, this will let them go to that page after log in
        next = request.args.get('next')
        if next is None or not next[0] == '/':
            next = url_for('core.index')
        return redirect(next)
    return render_template('login.html', form=form)
