import smtplib
from email.message import EmailMessage

def send_email(to , SUBJECT, TEXT):
    msg = EmailMessage()
    msg['Subject'] = SUBJECT
    msg['From'] = "host75102@gmail.com"
    msg['To'] = to
    msg.set_content(TEXT)

    print(f"[+] Sending email to {to}")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("host75102@gmail.com", "bhpnskvfvyaoecqr")
    server.send_message(msg)
    server.quit()
