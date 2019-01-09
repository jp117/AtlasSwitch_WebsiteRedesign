from flask import render_template, Blueprint


users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
