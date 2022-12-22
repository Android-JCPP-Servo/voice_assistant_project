# TODO List for Jack
This is a TODO list of things I'd like to add or modify for Jack

## Additions
1. Desktop Application Opener (i.e., Messenger, Slack, Pinball, etc.)
2. Grab and open link(s) from a .txt file instead of static array/list
3. Add new intent if stated command does not exist
    * If I state a command that does not exist in my current intents JSON file, the new command is added to the list with suggested patterns and responses
        * If this logic is successful, Jack will become artificially intelligent!
        * A big question I have is how to train the model again during usage (see Questions for better description)

## Modifications
1. File Editor - fix listen_to_audio() method

### Questions
1. If I add a new command with corresponding patterns and responses while using Jack, how can I retrain Jack with the new intents/commands?
2. If a new command is added, can I retrain Jack's model while using him?
3. Can models be retrained while being used or running?