import os
from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from madapp.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from flask_restful import Api
from flask_jwt_extended import JWTManager
from madapp import workers
from madapp.models import user, role

app = None
api = None
celery = None
cache = None

def createapp():
    currdir=os.path.abspath(os.path.dirname(__file__))
    app = Flask('__name__', template_folder='templates')
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(currdir,"trackerdb.sqlite3")
    app.config["SECRET_KEY"] = "verysecretkey"
    app.config["SECURITY_PASSWORD_HASH"] = 'bcrypt'
    app.config["SECURITY_PASSWORD_SALT"] = "reallysupersecret"
    app.config["SECURITY_REGISTERABLE"] = True
    app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
    app.config['JWT_SECRET_KEY'] = 'SECURITY_SECRET'
    app.config['JWT_TOKEN_LOCATION'] = 'headers'
    app.config['CELERY_BROKER_URL'] = "redis://localhost:6379/1"
    app.config['CELERY_RESULT_BACKEND']="redis://localhost:6379/2"
    app.config['REDIS_URL'] = "redis://localhost:6379"
    app.config['CACHE_TYPE']= "RedisCache"  
    app.config['CACHE_REDIS_HOST']="localhost"
    app.config['CACHE_REDIS_PORT']=6379
    app.config['CACHE_DEFAULT_TIMEOUT']= 300 

    db.init_app(app)
    api = Api(app)

    app.app_context().push()

    celery = workers.celery
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"]
    )
    celery.Task = workers.ContextTask
    app.app_context().push()

    cache = Cache(app)
    app.app_context().push()

    user_datastore = SQLAlchemySessionUserDatastore(db.session, user, role)
    security = Security(app, user_datastore)
    return(app, api, celery, cache)

app, api, celery, cache = createapp()
jwt = JWTManager(app)

CORS(app, resources={r'/*': {'origins': '*'}})

from madapp.controller import *
from madapp.api import *
 
api.add_resource(RegisterAPI, "/api/signup")
api.add_resource(LoginAPI, "/api/login")
api.add_resource(TrackersAPI, "/api/trackers")
api.add_resource(OneTrackerAPI, "/api/tracker/<int:trk_id>")
api.add_resource(LogsAPI, "/api/tracker/<int:trk_id>/logs")
api.add_resource(OneLogAPI,"/api/tracker/<int:trk_id>/logs/<int:log_id>")



if(__name__ == '__main__'):
    app.debug=True
    app.run(host='0.0.0.0')
