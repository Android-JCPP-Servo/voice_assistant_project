"""
MAPPINGS
This module is used to store and keep track of all mapped methods for SOC
"""

# Import all custom modules
from open_links import open_work, open_youtube, open_church, open_stonks, open_chrome
from doc_handler import create_file, edit_file, delete_file
from ward_council_email import send_test
from workday_assistant import start_workday

# Set the mappings object for Jack
mappings = {
    "file": create_file,
    "edit": edit_file,
    "delete": delete_file,
    "work day": start_workday,
    "work": open_work,
    "youtube": open_youtube,
    "church": open_church,
    "stonks": open_stonks,
    "chrome": open_chrome,
    "test email": send_test,
    # "not meeting": no_meeting,
    # "are meeting": yes_meeting
}

# Pass the mappings object back to Jack
def pass_mappings():
    return mappings