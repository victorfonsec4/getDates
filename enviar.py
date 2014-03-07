import smtplib
import os
from email.mime.text import MIMEText

def enviarEmail(menssagem, titulo):
	localDir = os.path.dirname(__file__)
	path = os.path.join(localDir, 'password.txt')

	open_file = open(path, 'r')
	password = open_file.readlines()
	open_file.close()

	msg = MIMEText(menssagem)


	recipients = ['victorcel@hotmail.com', 'claudionorsj@gmail.com', 'felipe.140492@gmail.com', 'ax.muzio@gmail.com', 'caiqueportolira@gmail.com']
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
