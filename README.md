# Flask + postgresql example:
Example how to handle postgresql in flask with:
1. Flask-SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/
2. Flask-Migrate https://flask-migrate.readthedocs.io/en/latest/#example

# Run app:
1. clone app
2. cd app_folder
3. create virtual environment: "python3 -m venv /path" or do it from IDE
4. activate venv
5. pip install --no-cache-dir -r requirements.txt
6. update "docker-compose.yml" with your own volumes paths
7. install PRE-COMMIT git hook: pre-commit install
8. run: "docker-compose up -d"

# .env and .psql_env
To change app settings update selected .env variables.
To change db settings update selected .psql_env variables.
