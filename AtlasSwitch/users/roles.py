from functools import wraps
from flask import url_for, redirect, flash
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.access_level == "admin":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page.")
            return redirect(url_for('employee_site/index'))
    return wrap


def sales_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.access_level == "admin" or current_user.access_level == 'sales':
            return f(*args, **kwargs)
        else:
            flash("You do not have permission to view this page.")
            return redirect(url_for('employee_site/index'))
    return wrap


def engineer_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.access_level == "admin" or current_user.access_level == 'engineer':
            return f(*args, **kwargs)
        else:
            flash("You do not have permission to view this page.")
            return redirect(url_for('employee_site/index'))
    return wrap
