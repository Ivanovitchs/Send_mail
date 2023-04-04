import smtplib
import conf
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ENVOYER DES EMAILS
# gmail

"""config_email
config_password
config_server
config_server_port"""

def envoyer_email(email_destinataire, sujet, message):

    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = conf.mailpersonnel
    multipart_message["To"] = email_destinataire

    multipart_message.attach(MIMEText(message, "plain"))

    serveur_mail = smtplib.SMTP(conf.mailsmtp, conf.portmail)
    serveur_mail.starttls()
    serveur_mail.login(conf.mailpersonnel, conf.motpasse)
    serveur_mail.sendmail(conf.mailpersonnel, email_destinataire, multipart_message.as_string())
    serveur_mail.quit()

message_email = """Bonjour,

Comment allez-vous ?

Merci.
"""

envoyer_email("jonathan@codeavecjonathan.com", "Email depuis Python", message_email)




