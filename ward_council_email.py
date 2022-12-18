# Import OS modules
import os

# Email sender modules
from email.message import EmailMessage
import ssl # For additional security
import smtplib

# Sound player imports
from play_sounds import play_greeting, play_response, play_command, play_goodbye

# Global variables for each email
my_email = 'astewart1138@gmail.com'
my_password = os.environ.get("jack_pass")
# test_email = 'theultimatemicrowave@gmail.com'
test_emails = ['theultimatemicrowave@gmail.com', 'anderson.stewart@streamit.live']
# Create Ward Council list
ward_council = []

# Method for sending email messages
def send_test():
    # Play R4-P17 response
    print("\nJack says:", "Sending email to your clients now...\n")
    play_response()
    # Set subject and body of email message
    subject = "New Test Email Message with separate functions using Jack"
    body = """
    This is a new test email using my new homemade voice assistant, Jack!
    """
    # Initialize email message
    em = EmailMessage()
    em['From'] = my_email
    em['To'] = test_emails
    em['Subject'] = subject
    em.set_content(body)
    # Set security
    context = ssl.create_default_context()
    # Pass data to sender handler
    send_email(my_email, my_password, test_emails, em, context)

# Method for sending negative message
def no_meeting():
    """
    TODO:
    1. Add email functionality to send negative message
    """

# Method for sending affirmative message
def yes_meeting():
    """
    TODO:
    1. Add email functionality to send affirmative message
    """

# Method for sending email through SMTP
def send_email(my_email, my_password, receivers, em, context):
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        # Login
        smtp.login(my_email, my_password)
        # Send email
        smtp.sendmail(my_email, receivers, em.as_string())