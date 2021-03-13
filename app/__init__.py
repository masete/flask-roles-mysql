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
        return render_template('home_page.html')

    # The Members page is only accessible to authenticated users
    # @app.route('/members')
    # @login_required    # Use of @login_required decorator
    # def member_page():
    #     return render_template_string("""
    #             {% extends "flask_user_layout.html" %}
    #             {% block content %}
    #                 <h2>{%trans%}Members page{%endtrans%}</h2>
    #                 <p><a href={{ url_for('user.register') }}>{%trans%}Register{%endtrans%}</a></p>
    #                 <p><a href={{ url_for('user.login') }}>{%trans%}Sign in{%endtrans%}</a></p>
    #                 <p><a href={{ url_for('home_page') }}>{%trans%}Home Page{%endtrans%}</a> (accessible to anyone)</p>
    #                 <p><a href={{ url_for('member_page') }}>{%trans%}Member Page{%endtrans%}</a> (login_required: member@example.com / Password1)</p>
    #                 <p><a href={{ url_for('admin_page') }}>{%trans%}Admin Page{%endtrans%}</a> (role_required: admin@example.com / Password1')</p>
    #                 <p><a href={{ url_for('user.logout') }}>{%trans%}Sign out{%endtrans%}</a></p>
    #             {% endblock %}
    #             """)

    # # The Admin page requires an 'Admin' role.
    # @app.route('/admin')
    # @roles_required('Admin')    # Use of @roles_required decorator
    # def admin_page():
    #     return render_template_string("""
    #             {% extends "flask_user_layout.html" %}
    #             {% block content %}
    #                 <h2>{%trans%}Admin Page{%endtrans%}</h2>
    #                 <p><a href={{ url_for('user.register') }}>{%trans%}Register{%endtrans%}</a></p>
    #                 <p><a href={{ url_for('user.login') }}>{%trans%}Sign in{%endtrans%}</a></p>
    #                 <p><a href={{ url_for('home_page') }}>{%trans%}Home Page{%endtrans%}</a> (accessible to anyone)</p>
    #                 <p><a href={{ url_for('member_page') }}>{%trans%}Member Page{%endtrans%}</a> (login_required: member@example.com / Password1)</p>
    #                 <p><a href={{ url_for('admin_page') }}>{%trans%}Admin Page{%endtrans%}</a> (role_required: admin@example.com / Password1')</p>
    #                 <p><a href={{ url_for('user.logout') }}>{%trans%}Sign out{%endtrans%}</a></p>
    #             {% endblock %}
    #             """)

    return app
