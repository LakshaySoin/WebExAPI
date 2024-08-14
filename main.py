from webexteamssdk import WebexTeamsAPI
import argparse
import os

def createRoom(token=None, roomId=None):
    counter = 1
    if (os.path.exists("counter.txt")):
        f = open("counter.txt", "r")
        counter = int(f.read())
    api = WebexTeamsAPI(access_token=token)
    filename = "{:03}".format(counter)
    api.messages.create(roomId, files=[f"./images/{filename}.jpg"])
    counter += 1
    if (counter == 366):
        counter = 1 
    f = open("counter.txt", "w")
    f.write(str(counter))

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', help="WebEx token", required=True)
    parser.add_argument('-r', '--room', help="WebEx room id", required=True)
    args = parser.parse_args()
    createRoom(args.token, args.room)