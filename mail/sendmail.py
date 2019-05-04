import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
import time
from datetime import datetime
import yaml
import os


path =  os.path.dirname(os.path.realpath(__file__))
config_path = path+"/../testdata/config.yml"

mail_file_name = path +"/../test-reports/report/mail_Report.html"


with open(config_path, 'r') as f:
  config = yaml.load(f)
msg = MIMEMultipart()
recipients = [config['to_mail1'], config['to_mail2']]
msg['Subject'] = config['project_name'] + config['subject']
msg['From'] = config['from_mail']
msg['To'] = ", ".join(recipients)

with open (mail_file_name, "r") as myfile:
    data=myfile.read().replace('\n', '')

mail_body = data.replace("[x]","")
mail_body = mail_body.replace("Show","");
mail_body = mail_body.replace("Summary","");
mail_body = mail_body.replace("Failed","");
mail_body = mail_body.replace("All","");

text = MIMEText(mail_body,'html')
msg.attach(text)
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(config['from_mail'], config['from_password'])
s.sendmail(config['from_mail'], recipients, msg.as_string())
s.quit()
