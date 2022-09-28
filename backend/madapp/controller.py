from flask import Flask, send_file
from flask import current_app as app
from .tasks import *
import csv
from main import cache

@cache.memoize(timeout=50)
@app.route('/logcsv/<int:trk_id>')
def logcsv(trk_id):
    Logjob=sendLogCSV.delay(trk_id)
    fields=['id','value','time','note']
    res=Logjob.wait()
    with open("static/Logs.csv",'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = fields)
        writer.writeheader() 
        writer.writerows(res)
    return send_file("static/Logs.csv",as_attachment=True)

@cache.memoize(timeout=50)
@app.route('/trackercsv/<string:username>')
def trackcsv(username):
    Trackjob=sendTrackCSV.delay(username)
    fields=['id','name','description','type','settings']
    res=Trackjob.wait()
    with open("static/Trackers.csv",'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames = fields)
        writer.writeheader() 
        writer.writerows(res)
    return send_file("static/Trackers.csv",as_attachment=True)

