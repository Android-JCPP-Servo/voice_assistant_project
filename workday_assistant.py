# Import custom modules
from open_links import open_work, open_youtube, open_stonks
from play_sounds import play_command

"""
WORKDAY ASSISTANT
This program is for when I state I'm now working
"""
def start_workday():
    # Let me know what you're doing, Jack!
    print("\nJack says:", "Opening your workday links now!\n")
    play_command()
    open_work() # Open work link
    open_youtube() # Open youtube
    open_stonks() # Open stonks