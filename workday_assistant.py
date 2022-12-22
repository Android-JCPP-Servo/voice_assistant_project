# Import webbrowser module
import webbrowser

# Import custom modules
from open_links import open_work, open_youtube, open_stonks
from play_sounds import play_response, play_command

"""
WORKDAY ASSISTANT
This program is for when I state I'm now working
"""
def start_workday():
    # Let me know what you're doing, Jack!
    print("\nJack says:", "Opening your workday links now!\n")
    play_command()
    # Set array of all links
    workday_links = ['https://cyberlandr.a2hosted.com/web', 'https://www.youtube.com/', 'https://portfolio.primerica.com/']
    # Loop through array and open links
    for i in workday_links:
        webbrowser.open_new(i)
    # As Jack's opening links, play response voice and open all links at once...
    play_response()