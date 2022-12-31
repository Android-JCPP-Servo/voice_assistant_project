# Import OS modules
import os
import datetime

# DOTENV modules and methods
from dotenv import load_dotenv
load_dotenv()

# Email sender modules
from email.message import EmailMessage
import ssl # For additional security
import smtplib

# Sound player imports
from play_sounds import play_greeting, play_response, play_command, play_goodbye

# Get emails
from read_csv_test import get_emails

# Global variables for each email
my_email = 'astewart1138@gmail.com'
# My return address
my_return = 'Andersen Stewart <astewart1138@gmail.com>'
my_password = os.getenv('JACK_PASS')
test_emails = ['theultimatemicrowave@gmail.com', 'astewart1138@gmail.com']

# Create Ward Council list ONLY if password exists
if my_password is not None:
    ward_council = get_emails() # Create council list
else:
    ward_council = [] # Create empty list

# Get date value for Sunday (this email is usually sent on Saturday, so I want Jack to list the date for the next day)
todayDate = datetime.datetime.today()
nextDayDate = todayDate + datetime.timedelta(days=1)
nextDayDate = nextDayDate.strftime('%m/%d/%Y') # Set date to usual format
nextDayDate = str(nextDayDate) # Set date to string

# Method for sending email messages
def send_test():
    # Play R4-P17 response
    print("\nJack says:", "Sending email to your clients now...\n")
    play_response()
    try:
        # Set subject and body of email message
        subject = "Test Email with Jack - " + todayDate
        body = """
        This is a text email with my personal voice assistant, Jack!
        """
        # Initialize email message
        em = EmailMessage()
        em['From'] = my_return
        em['To'] = test_emails
        em['Subject'] = subject
        em.set_content(body)
        # Set security
        context = ssl.create_default_context()
        # Pass data to sender handler
        send_email(my_email, my_password, test_emails, em, context)
    except Exception as e:
        print("\nJack says:", "I had an error here:", e, '\n')

# Method for sending negative message
def no_meeting():
    # Play R4-P17 response
    print("\nJack says:", "Sending email to your clients now...\n")
    play_response()
    try:
        # Set subject and body of email message
        subject = "No Ward Council - " + nextDayDate
        body = """
        Howdy Ward Council,

        There is no Ward Council tomorrow morning.
        
        See y'all at church!

        Andersen
        """
        # Initialize email message
        em = EmailMessage()
        em['From'] = my_return
        em['To'] = test_emails
        em['Subject'] = subject
        em.set_content(body)
        # Set security
        context = ssl.create_default_context()
        # Pass data to sender handler
        send_email(my_email, my_password, test_emails, em, context)
    except Exception as e:
        print("\nJack says:", "I had an error here:", e, '\n')

# Method for sending affirmative message
def yes_meeting():
    # Play R4-P17 response
    print("\nJack says:", "Sending email to your clients now...\n")
    play_response()
    try:
        # Set subject and body of email message
        subject = "Ward Council - " + nextDayDate + " @ 8:30am"
        body = """
        Howdy Ward Council,

        We'll be having Ward Council at 8:30am tomorrow morning.
        
        See y'all then!

        Andersen
        """
        # Initialize email message
        em = EmailMessage()
        em['From'] = my_return
        em['To'] = test_emails
        em['Subject'] = subject
        em.set_content(body)
        # Set security
        context = ssl.create_default_context()
        # Pass data to sender handler
        send_email(my_email, my_password, test_emails, em, context)
    except Exception as e:
        print("\nJack says:", "I had an error here:", e, '\n')

# Method for sending email through SMTP
def send_email(my_email, my_password, receivers, em, context):
    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        # Login
        smtp.login(my_email, my_password)
        # Send email
        smtp.sendmail(my_email, receivers, em.as_string())