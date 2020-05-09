import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'PyPI'
email['to'] = 'sowrarajk@gmail.com'
email['subject'] = 'Hi Baby'

email.set_content('Parotta parottaa sowra sutta parottaa')

with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jacapo77@gmail.com', 'amardeniro')
    smtp.send_message(email)
    print('all good boss!')
