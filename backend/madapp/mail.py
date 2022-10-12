from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from weasyprint import HTML

SMPTP_SERVER_HOST= "localhost"
SMPTP_SERVER__PORT= 1025
SENDER_ADDRESS= "shagun@test.com"
SENDER_PASSWORD= ""

def sendEmail(to,sub,mess):
    msg=MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['To'] = to
    msg['Subject']=sub

    msg.attach(MIMEText(mess,"plain"))

    try:
        s= smtplib.SMTP(host=SMPTP_SERVER_HOST,
                        port=SMPTP_SERVER__PORT)
        s.login(SENDER_ADDRESS,SENDER_PASSWORD)
        s.send_message(msg)
        s.quit()
    except :
        return False
    return True

def sendReportEmail(to,sub,mess):
    msg=MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['To'] = to
    msg['Subject']=sub

    msg.attach(MIMEText(mess,"html"))
    
    html = HTML(string=mess)
    html.write_pdf(target='static/Report.pdf')

    with open('static/Report.pdf', "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str('static/Report.pdf'))
    msg.attach(attach)

    try:
        s= smtplib.SMTP(host=SMPTP_SERVER_HOST,
                        port=SMPTP_SERVER__PORT)
        s.login(SENDER_ADDRESS,SENDER_PASSWORD)
        s.send_message(msg)
        s.quit()
    except :
        return False
    return True
