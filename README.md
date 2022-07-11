# Flask + postgresql example:
Example how to handle postgresql in flask with:
1. Flask-SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/
2. Flask-Migrate https://flask-migrate.readthedocs.io/en/latest/#example

# Run app:
1. clone app
2. cd app_folder
3. update "docker-compose.yml" with your own volumes paths
4. run: "docker-compose up -d"
5. migrate DB:
   1. flask db migrate
   2. flask db upgrade
6. run app: flask run
7. install PRE-COMMIT git hook: pre-commit install

# .env and .psql_env
To change app settings update selected .env variables.
To change db settings update selected .psql_env variables.
