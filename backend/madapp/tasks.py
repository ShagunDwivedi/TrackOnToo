from madapp.workers import celery
from madapp.models import log, user, tracker
from celery.schedules import crontab
from madapp.mail import sendEmail, sendReportEmail
import datetime
from flask import render_template


@celery.task
def sendMailToAll():
    users=user.query.all()
    for user1 in users:
        #print(user1.name)
        logs = log.query.filter_by(user_id=user1.id).all()
        if(logs == []):
            #print(logs, user1)
            sendEmail(to=user1.email,
                sub='Tracker Reminder',
                mess='''Hello {},\n
Hope that you are doing great.
Don't forget to log into your Trackers.
Have a great day!\n
Regards,
TrackOn App.
'''.format(user1.name))
        elif(datetime.date.today() != logs[-1].time.strftime("%Y-%m-%d")):
            #print(logs, user1)
            sendEmail(to=user1.email,
            sub='Tracker Reminder',
            mess='''Hello {},\n
Hope that you are doing great.
Don't forget to log into your Trackers.
Have a great day!\n
Regards,
TrackOn App.
'''.format(user1.name))

@celery.task
def sendMonthlyMail():
    users=user.query.all()
    for user1 in users:
        listmess = []
        #print(user1.name)
        trackers = tracker.query.filter_by(user_id=user1.id).all()
        if(trackers == []):
            htm = render_template('email.htm', uname=user1.name, trackerlist=listmess)
            sendReportEmail(to=user1.email,
            sub="Monthly Progress Report",
            mess=htm)
        else:
            for trkr in trackers:
                trackdict = {'trackername': trkr.trk_name, 'lowest': '', 'highest': '', 'no': ''}
                logs = log.query.filter_by(trk_id=trkr.trk_id).all()
                #if(trkr.trk_type == 1 or trkr.trk_type == )
                loglist = []
                date1 = datetime.date.today() - datetime.timedelta(1)
                for log1 in logs:
                    if(log1.time.strftime("%Y-%m") == date1.strftime("%Y-%m")):
                        if(trkr.trk_type == 1):
                            loglist.append(int(log1.value))
                        elif(trkr.trk_type == 4 and log1.value != ''):
                            #print(log1.value[:2])
                            loglist.append(int(log1.value[:2]))
                        else:
                            loglist.append(log1.value)
                if(trkr.trk_type == 1 or trkr.trk_type == 4):
                    trackdict['lowest'] = min(loglist)
                    #print(min(loglist))
                    trackdict['highest'] = max(loglist)
                    trackdict['no'] = len(loglist)
                    listmess.append(trackdict)
                    #print(listmess)
                else:
                    sett = trkr.settings.split(',') if trkr.settings else ['Yes', 'No']
                    countc = {}
                    for i in sett:
                        countc[i] = loglist.count(i)
                    for i in countc.keys():
                        if(countc[i] == max(countc.values())):
                            trackdict['highest'] = i
                        elif(countc[i] == min(countc.values())):
                            trackdict['lowest'] = i
                    trackdict['no'] = len(loglist)
                    listmess.append(trackdict)
                    #print(trackdict)
                    
                    

            #print(listmess)        
            htm = render_template('email.htm', uname=user1.name, trackerlist=listmess)
            sendReportEmail(to=user1.email,
            sub="Monthly Progress Report",
            mess=htm)
        #print(listmess)        



@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=12, minute=30),
        sendMailToAll.s(),
        name="Daily Mail"
        )
    sender.add_periodic_task(
        crontab(0, 0, day_of_month='1'),
        sendMonthlyMail.s(),
        name="Monthly Report Mail"
    )


@celery.task
def sendLogCSV(trk_id):
    '''
    an async function to return the list of JSON of logs...
    '''
    logs = log.query.filter_by(trk_id= trk_id).all()
    #print(logs)
    return [log1.toJson() for log1 in logs]

@celery.task
def sendTrackCSV(user_id):
    '''
    an async function to return the list of JSON of trackers...
    '''
    trks = tracker.query.filter_by(user_id= user_id).all()
    #print(trks)
    return [trkr.toJson() for trkr in trks]
