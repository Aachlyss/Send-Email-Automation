import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email from Python"
email_sender = "ivanangelov05@gmail.com"
email_receiver = "ivanangelov05@gmail.com"
password = input("Enter password: ")

message = EmailMessage()
message["From"] = email_sender
message["To"] = email_receiver
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, message.as_string)
print("Email Sent!")