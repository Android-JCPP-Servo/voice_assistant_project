"""
MAPPINGS
This module is used to store and keep track of all mapped methods for SOC
"""

# Import all custom modules
from doc_handler import create_file, edit_file, delete_file
from ward_council_email import send_test, confirm_no, confirm_yes
from workday_assistant import start_workday
from open_app import open_app

# Set the mappings object for Jack
mappings = {
    "file": create_file,
    "edit": edit_file,
    "delete": delete_file,
    "work day": start_workday,
    "test email": send_test,
    "not meeting": confirm_no,
    "are meeting": confirm_yes,
    "open app": open_app,
}

# Pass the mappings object back to Jack
def pass_mappings():
    return mappings