import smtplib
import  conf

"""
mailpersonnel="ij.ngoudjo@gmail.com"
motpasse="vealbltwnvlcugag"
mailsmtp="smtp.gmail.com"
portmail=587

"""
def envoiemail(maildestinataire,message):
    #l'objet de creation de mails
  serveur_mail=  smtplib.SMTP(conf.mailsmtp,conf.portmail)
  #securisation du mail
  serveur_mail.starttls()
  #connexion au serveur
  serveur_mail.login(conf.mailpersonnel,conf.motpasse)
  serveur_mail.sendmail(conf.mailpersonnel,maildestinataire,message)
  serveur_mail.quit

envoiemail("ij.ngoudjo@gmail.com","Bonjour")
    