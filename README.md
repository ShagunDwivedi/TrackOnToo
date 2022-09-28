# _QuantifiedSelf App_

 QuantifiedSelf is a web application used for tracking habits, activities, other life parameters. Users can Register & Login to create multiple Trackers with multiple logs. They can review their progress over time with graphs trend lines.

## Prerequisites

NOTE: ```This won't work on Windows as it needs Redis and which is not supported on Windows, instead one needs WSL or Docker.```

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
│   │   ├── mail.py
│   │   ├── models.py
│   │   ├── plotforapp.py
│   │   ├── tasks.py
│   │   └── workers.py
│   ├── static
│   │   ├── Logs.csv
│   │   ├── plot.jpg
│   │   └── Trackers.csv
│   ├── templates
│   │   └── email.htm
│   ├── app_apis.yaml
│   ├── celerybeat-schedule
│   ├── trackerdb.sqlite3
│   ├── local_beat.sh
│   ├── local_run.sh
│   ├── local_setup.sh
│   ├── local_workers.sh
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
├── frontend
│   ├── babel.config.js
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
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
    source  local_setup.sh
    ```

  * ```bash
    source local_run.sh
    ```

  * ```bash
    source local_beat.sh
    ```

  * ```bash
    source local_workers.sh
    ```

* Setting up frontend:

  * ```bash
    cd  frontend/
    ```

  * ```javascript
    npm install
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
* Export Logs as a CSV (Asynchronous Task)
* Log into Tracker
* Daily Scheduled Reminders as mails
* Sends Monthly Progress Report as mails

## To-Do's

* Send Monthly Progress Report as PDF
* Add Import Option for Trackers and Logs
* Improve UI / Add Animations for Tracker Review