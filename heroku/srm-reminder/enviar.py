import smtplib
from email.mime.text import MIMEText

def enviarEmail(menssagem, amanha):
	msg = MIMEText(menssagem)
	
	if(amanha == True):
		subject = 'SRM Amanha'
	else:
		subject = 'SRM Hoje'

	msg['Subject'] = subject
	msg['From'] = 'Victor'
	msg['To'] = 'victorcel@hotmail.com'

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('victorSmtpServer@gmail.com', 'disposable')
	server.sendmail('Victor', ['victorcel@hotmail.com'], msg.as_string())
	server.close()
