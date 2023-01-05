"""
OPEN LINKS

Methods for handling workday tasks
"""
# DOTENV modules and methods
import os
from dotenv import load_dotenv
load_dotenv()

# Import webbrowser module
import webbrowser

# Import sound responses
from play_sounds import play_response

# Daily URLs
work_url = os.getenv('WORK_URL')
music_url = os.getenv('MUSIC_URL')
church_url = os.getenv('CHURCH_URL')
stonks_url = os.getenv('STONKS_URL')
chrome_url = os.getenv('CHROME_URL')
stripe_url = os.getenv('STRIPE_URL')
school_url = os.getenv('SCHOOL_URL')
codecademy_url = os.getenv('CODECADEMY_URL')
gmail_url = os.getenv('GMAIL_URL')

# Method for splitting text
def split_sentence(text):
    # Set daily task array
    tasks = ['work', 'stripe', 'youtube', 'church', 'stonks', 'chrome', 'school', 'codecademy', 'gmail']
    # Split text
    text = text.split()
    # Set operation definer
    done = False
    # Loop through text and tasks
    for i in tasks:
        for j in text:
            # If there's a match...
            if j == i:
                # Pass it to open_command
                open_command(i)
                # Return true to halt Assistant operation
                done = True
                print("Match?", done)
                return done
    # If there's no match, return false to proceed with Assistant operation
    print("Match?", done)
    return done
    
# Method for handling specific page command
def open_command(word):
    match word:
        case 'work':
            webbrowser.open_new(work_url)
            print("\nJack says:", "Good luck at work today!\n")
        case 'stripe':
            webbrowser.open_new(stripe_url)
            print("\nJack says:", "Sounds like Bill's got'cha busy!\n")
        case 'youtube':
            webbrowser.open_new(music_url)
            print("\nJack says:", "Grabbing music from YouTube now...\n")
        case 'church':
            webbrowser.open_new(church_url)
            print("\nJack says:", "Taking you to church...\n")
        case 'stonks':
            webbrowser.open_new(stonks_url)
            print("\nJack says:", "Pulling up your stonks...\n")
        case 'chrome':
            webbrowser.open_new(chrome_url)
            print("\nJack says:", "Opening Chrome now!\n")
        case 'school':
            webbrowser.open_new(school_url)
            print("\nJack says:", "Good luck in school today!\n")
        case 'codecademy':
            webbrowser.open_new(codecademy_url)
            print("\nJack says:", "What certification will you do today?\n")
        case 'gmail':
            webbrowser.open_new(gmail_url)
            print("\nJack says:", "Pulling up email and clients now...\n")
    
    # Play R4-P17 response
    play_response()