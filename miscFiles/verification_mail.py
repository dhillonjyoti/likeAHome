import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def verify_link_send(to_address, name, link):
    msg = MIMEMultipart()
    msg['From'] = "Like A Home"
    msg['To'] = to_address
    msg['Subject'] = "Email Verification Link"

    body = "Hey {}! Your verify link is {}".format(str(name), str(link))

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login('rishjaitly@gmail.com', '9501110692')
    text = msg.as_string()
    server.sendmail("rishjaitly@gmail.com", to_address, text)