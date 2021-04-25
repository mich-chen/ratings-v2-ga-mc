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
        - (env) $ flask run --port --debug --env
        - setting env variables specify flask how to load the app
        - can maintain code independent of external env configs

    - run flask as python module, explicitly setting python interpreter to call Flask CLI
        - (env) $ python3 -m flask run
        - python executable on PATH and runs the module flask and runs the flask app.
        - enables you to run diff Flask from first
        - enables you to also run diff python interpreter

Author: Michelle Chen
"""