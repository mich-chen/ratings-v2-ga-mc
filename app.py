"""
Practice Flask app with SQLAlchemy and postgres DB.

Requirements:
    - Python 3.*
    - PostgreSQL
    - Flask
    - SQLAlchemy
    - Pytest

Running Flask options:
    - running python script through if __name__ == '__main__': app.run()
        - launch local server same way flask script does
        - not recommended by Flask docs due to reload mechanisms and possible bizarre side-effects
        - side effects (execute certain code 2x, crashing without message or syntax or import errors)
        - also problematic when modifying configs (can get a bit messy to modify code base)

    - run flask CLI tool script with:
        - (env) $ export FLASK_APP=app.py
        - (env) $ export FLASK_ENV=development
        - (env) $ export FLASK_DEBUG=1     # 1 to enable, 0 to disable
        - (env) $ export FLASK_RUN_PORT=5000
        - (env) $ flask run --port --debug --env --host
        - setting env variables specify flask how to load the app
        - can maintain code independent of external env configs

    - run flask as python module, explicitly setting python interpreter to call Flask CLI
        - (env) $ python3 -m flask run
        - python executable on PATH and runs the module flask and runs the flask app.
        - enables you to run diff Flask from first
        - enables you to also run diff python interpreter

Author: Michelle Chen
"""

from flask import Flask, render_template, request, session, Blueprint

# set up flask app
app = Flask(__name__)
app.secret_key = 'dev'

# catch-all route
@app.route('/', defaults={'path': ''})
@app.route('/<string:path>') # specifying anything string in path
@app.route('/<path:path>')
def catch_all(path):
    """Catch all URL routes that don't match specific path."""
    return render_template('homepage.html')

@app.route('/')
def homepage():
    """Render homepage."""
    return render_template('homepage.html')

# Blueprint(blueprint name, Blueprint's import name (used to locate blueprint's resources))
movies_page = Blueprint()

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        all_users = crud.get_all_user()
        return render_template('all_users.html', users=all_users)

    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)

        if user:
            flash('You cannot create an account with that email. Try again.')
        else:
            crud.create_user(email=email, password=password)
            flash('Account created successfully!')
        return redirect('/')
