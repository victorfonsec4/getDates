import smtplib
from email.mime.text import MIMEText

def enviarEmail(menssagem, titulo):
	open_file = open('password.txt', 'r')
	password = open_file.readlines()
	open_file.close()

	msg = MIMEText(menssagem)
	
	
	recipients = ['victorcel@hotmail.com', 'claudionorsj@gmail.com']
	msg['Subject'] = titulo
	msg['From'] = 'Victor'
	msg['To'] = ", ".join(recipients)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('victorSmtpServer@gmail.com', password[0])
	server.sendmail('Victor', recipients, msg.as_string())
	server.close()
