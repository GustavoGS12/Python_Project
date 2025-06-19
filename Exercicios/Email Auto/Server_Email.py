import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = ''
port = ''
login = ''
senha = ''

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login, senha)

newEmail = MIMEMultipart()
mensagem = 'Teste'
newEmail['From'] = login
newEmail['To'] = 'bbenjamim13@gmail.com'
newEmail['Subject']
newEmail.attach(MIMEText(mensagem, 'plain'))

server.quit()


