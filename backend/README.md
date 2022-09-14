# Local Setup
- Clone the project
- Run `setup.sh`

# Local Development Run
- `local_run.sh` It will start the flask app in `development`. Suited for local development

# Replit Run
- Go to shell and run
    `pip install --upgrade poetry`
- Click on `main.py` and click button Run
- Project is at https://mad1trackon.shagundwivedi.repl.co/

# Folder Structure

- `trackerdb`  is the sqlite database.
- `madapp` is where the code for the app is.
- `setup.sh` sets up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project.
- `local_run.sh`  is used to run the flask application in development mode.
- `static` - default `static` files folder. It serves at '/static' path, and has images required .
- `templates` - Default flask templates folder.
- `app_apis.yaml` has the API documentation.


```
├── local_run.sh
├── local_setup.sh
├── madapp
│   ├── api.py
│   ├── controller.py
│   ├── database.py
│   ├── for_security.py
│   ├── models.py
│   ├── plotforapp.py
│   └── __pycache__
|       ├── api.cpython-310.pyc
│       ├── controller.cpython-310.pyc
│       ├── database.cpython-310.pyc
|       ├── for_security.cpython-310.pyc
│       ├── models.cpython-310.pyc
│       └── plotforapp.cpython-310.pyc
├── main.py
├── readme.md
├── static
│   ├── login.jpg
│   ├── minimalism1.gif
│   └── plot.jpg
├── templates
|   ├── security
|   |   ├── _formhelpers.html
|   |   ├── login_user.html
│   |   └── register_user.html
│   ├── addlog.html
│   ├── addtracker.html
│   ├── dash.html
│   ├── homepage.html
│   ├── logs.html
│   ├── updatelog.html
│   └── updatetracker.html
└── trackerdb.sqlite3
```