import smtplib
import imghdr
from email.message import EmailMessage

sender = "varunhs2409@gmail.com"
receiver = "varunhs117@gmail.com"
password = "fdia iaio eekf knkp"


def send_mail(image_path):
    email_msg = EmailMessage
    email_msg.Subject = "New object detected !"

    with open(image_path, "rb") as file:
        content = file.read()
    email_msg.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com, 587")
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_msg.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_mail(image_path="images/2.png")
