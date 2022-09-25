# _QuantifiedSelf App_

 QuantifiedSelf is a web application used for tracking habits, activities, other life parameters. Users can Register & Login to create multiple Trackers with multiple logs. They can review their progress over time with graphs trend lines.

## Prerequisites

NOTE: ```This won't work on Windows as we need Redis and it is not supported on Windows, instead you will need WSL or Docker, however a Linux Sytem would be best as you would be able to use all .sh files that help in setup and running```

1) [Python3](https://www.python.org/downloads/) and [Pip3](https://pypi.org/project/pip/)
2) [NodeJS](https://nodejs.org/en/)
3) [Redis](https://redis.io/) & [RESP](https://resp.app/)
4) [MailHog](https://github.com/mailhog/MailHog)

## Project Structure

``` bash
.
├── backend
│   ├── madapp
│   │   ├── api.py
│   │   ├── controller.py
│   │   ├── for_security.py
│   │   ├── mail.py
│   │   ├── plotforapp.py
│   │   ├── tasks.py
│   │   └── workers.py
│   ├── celerybeat-schedule
│   ├── trackerdb.sqlite3
│   ├── Trackers.csv
│   ├── Logs.csv
│   ├── local_beat.sh
│   ├── local_run.sh
│   ├── local_setup.sh
│   ├── local_worker.sh
│   ├── main.py
│   └── requirements.txt
├── frontend
│   ├── babel.config.js
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   └── index.html
│   ├── README.md
│   ├── src
│   │   ├── assets
│   │   ├── App.vue
│   │   ├── components
│   │   │   ├── Dashboard.vue
│   │   │   ├── Error.vue
│   │   │   ├── Home.vue
│   │   │   ├── LogAdd.vue
│   │   │   ├── LogDel.vue
│   │   │   ├── Login.vue
│   │   │   ├── LogUpd.vue
│   │   │   ├── Register.vue
│   │   │   ├── Tracker.vue
│   │   │   ├── TrackerAdd.vue
│   │   │   ├── TrackerDel.vue
│   │   │   └── TrackerUpd.vue
│   │   ├── main.js
│   │   ├── router
│   │   │   └── index.js
│   │   ├── store
│   │   │   └── index.js
│   │   └── views
│   │       ├── Dashboard.vue
│   │       ├── Error.vue
│   │       ├── Home.vue
│   │       ├── LogAdd.vue
│   │       ├── LogDel.vue
│   │       ├── Login.vue
│   │       ├── LogUpd.vue
│   │       ├── Register.vue
│   │       ├── Tracker.vue
│   │       ├── TrackerAdd.vue
│   │       ├── TrackerDel.vue
│   │       └── TrackerUpd.vue
│   └── .editorconfig
└── README.md
```

## Setup

* Setting Up Backend:

  * ```bash
    cd  backend/
    ```

  * ```bash
    source  localsetup.sh
    ```

  * ```bash
    source localrun.sh
    ```

  * ```bash
    source localbeat.sh
    ```

  * ```bash
    source localworker.sh
    ```

* Setting up frontend:

  * ```bash
    cd  frontend/
    ```

  * ```javascript
    npm i
    ```

  * ```javascript
    npm run serve
    ```

* Setting Up MailHog:

  ```bash
  ~/go/bin/MailHog
  ```

## Tech Stack Used

* Frontend : ```Vue.Js```
* Backend : ```Flask```
* API : ```Flask Restful```
* Authentication : ```JWT token```
* Database : ```Sqlite3```
* ORM : ```Flask-SQL Alchemy```
* Cache : ```Redis```
* Message Broker : ```Redis```
* Task-Queue : ```Celery```

## Features

* Secure Login Using JWT
* Tracker Management using APIs
* Export a Tracker as a CSV (Asynchronous Task)
* Log into Tracker
* Daily Scheduled Reminders

## To-Do's

* Add feature to import a CSV to create tracker
* Add Jinja Template to Mails
* Send Monthly Progress Report as PDF
* Improve UI / Add Animations for Tracker Review