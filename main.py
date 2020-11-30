#!/usr/bin/env python3

try:
    # all the imports needed
    from termcolor import colored
    from getpass import getpass
    import requests
    import random
    import json


    # function to check if token is valid
    def check_token(token: str):
        r = requests.get("https://discordapp.com/api/v6/auth/login", headers = {
            "Authorization": token
        })
        if r.status_code == 200:
            return True
        else:
            return False

    def send_msg(token: str, channelID: int, guildID: int, message, replyID: int):
        return requests.post(f"https://discordapp.com/api/channels/{channelID}/messages", headers = {
            "authorization": token,
            "content-type": "application/json"
        }, data = json.dumps({
            "content": message,
            "nonce": str(random.randrange(5000,5000000)),
            "message_reference": {
                "guild_id": guildID,
                "channelID": channelID,
                "message_id": replyID,
        },
            "allowed_mentions": {
                "parse": ["users", "roles", "everyone"],
                "replied_user": True
            }
        })
    )


    running = False


    # token input
    token_input = True
    while token_input:
        token = getpass(f"[{colored('*', 'red')}] Token: ")
        check = check_token(token)
        if check == True:
            print(colored('Token is valid', 'green'))
            token_input = False
            running = True
        else:
            print(colored('Token is invalid', 'red'))
            continue

    # while its ready to be used
    while running:
        guildID = int(input("Enter guild id: "))
        channelID = int(input("Enter channel id: "))
        messageContent = input("Contents of the message you want to send with a server badge: ")
        replyID = int(input('Enter the id of a reply: '))
        r = send_msg(token, channelID, guildID, messageContent, replyID)
        if r.status_code == 200:
            print(colored('Message sent', 'green'))
        else:
            print(colored('Fail sending the message', 'red'))


# error handling for when user attempts to input wrong data types
except ValueError:
    print("Make sure the value is right")
    exit()

# error for keyboard interrupt: attempt to close the script
except KeyboardInterrupt:
	print(colored('\nBye!', 'green'))
	exit()

# error importing packages
except ImportError:
    print('''Please install packages from requirements.txt
Use command "pip install -r requirements.txt" to install all the required plugins''')
