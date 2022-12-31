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

# Method for opening specific typical workday links
def open_work():
    # Open CyberLandr website
    webbrowser.open_new(work_url)
    # Play R4-P17 response
    print("\nJack says:", "Good luck at work today!\n")
    play_response()

# Method for opening YouTube
def open_youtube():
    # Open YouTube
    webbrowser.open_new(music_url)
    # Play R4-P17 response
    print("\nJack says:", "Grabbing music from YouTube now...\n")
    play_response()

# Method for opening church website
def open_church():
    # Open church website
    webbrowser.open_new(church_url)
    # Play R4-P17 response
    print("\nJack says:", "Taking you to church...\n")
    play_response()

# Method for showing stonks
def open_stonks():
    # Open Stonks
    webbrowser.open_new(stonks_url)
    # Play R4-P17 response
    print("\nJack says:", "Pulling up your stonks...\n")
    play_response()

# Method for opening Chrome
def open_chrome():
    # Open Stonks
    webbrowser.open_new(chrome_url)
    # Play R4-P17 response
    print("\nJack says:", "Opening Chrome now!\n")
    play_response()