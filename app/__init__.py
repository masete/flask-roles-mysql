import datetime
from flask import Flask, request, render_template
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from app.config import ConfigClass
# from app.models import User
# Class-based application configuration


def create_app():
    """ Flask application factory """
    
    # Create Flask app load app.config
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    # Initialize Flask-BabelEx
    babel = Babel(app)

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    # Define the User data-model.
    # NB: Make sure to add flask_user UserMixin !!!
   
    # The Home page is accessible to anyone
    @app.route('/')
    @app.route('/home_page', methods=['POST', 'GET'])
    def home_page():
        return render_template("home_page.html")

    
    @app.route('/register', methods=['POST', 'GET'])
    def register():
        return render_template("register.html")

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        return render_template("login.html")

    @app.route('/logout', methods=['POST', 'GET'])
    def logout():
        return render_template("logout.html")

    # The Members page is only accessible to authenticated users
    @app.route('/members')
    @login_required    # Use of @login_required decorator
    def member_page():
        return render_template('member_page')

    # The Admin page requires an 'Admin' role.
    @app.route('/admin')
    @roles_required('Admin')    # Use of @roles_required decorator
    def admin_page():
        return render_template('admin_page')

    return app
