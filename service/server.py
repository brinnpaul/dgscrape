import smtplib, socket

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Server(object):
    def __init__(self, config):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_FROM, config.EMAIL_PASSWORD)
            self.server = server
        except socket.error as e:
            print e

    def __enter__(self):
        return self.server

    def __exit__(self, *ext):
        self.server.quit()

class Mail(object):

    def __init__(self, config):
        self.__config = config
        self.send = None

    def __format(self, message):
        config = self.__config
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "DGScrape Results"
        msg['From'] = config.EMAIL_FROM
        msg['To'] = config.EMAIL_TO
        message = MIMEText(message, 'plain')
        msg.attach(message)
        return msg

    def make_sender(self, server, message):
        config = self.__config
        email = self.__format(message)
        def send_mail():
            server.sendmail(config.EMAIL_FROM, config.EMAIL_TO, email.as_string())
        self.send = send_mail
