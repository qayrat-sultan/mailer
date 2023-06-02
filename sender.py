import smtplib
from email.message import EmailMessage

from main import found_emails
from text import send_text

# Set up the email details
sender_email = "kairat@mtour.kz"
sender_password = "smtppassword"
subject = "MTour - первый маркетплейс для поиска места лечения и отдыха в Казахстане!"
body = send_text
with open("sended_emails.txt", "r") as file:
    already_sent_emails = file.read().splitlines()
filtered_recipient_emails = [email for email in found_emails if email not in already_sent_emails][:20]
# Create the email message
message = EmailMessage()
message["Subject"] = subject
message["From"] = sender_email
message["To"] = ", ".join(filtered_recipient_emails)
message.set_content(body)

# Send the email
with smtplib.SMTP("smtp.mail.ru", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)

with open("sended_emails.txt", "a") as f:
    f.write("\n".join(filtered_recipient_emails))
    f.write("\n")
