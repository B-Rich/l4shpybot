#! /usr/bin/python

###############################################################################
# Program = l4shpybot
# Description = IRC bot written in python
# Author = Luis Salazar (l4sh)
# License = zlib like license - Copyright (c) 2013, Luis Salazar (l4sh)
# Version = none yet, let's call it alpha
#
# For more info check README.md
# For details about the license check LICENSE.txt
#
###############################################################################

#imports
import socket
import irccommands
import botcommands
import config


#### Establish connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((config.server, config.port))

## Identify bot
s.send(irccommands.nick(config.nick))

s.send(irccommands.user(config.nick, config.realname, config.server))

## Program loop
while True:

    data = s.recv(4096)

    # check for pings and reply
    if data.split()[0] == 'PING':
        s.send(irccommands.pong(data))
        print('PONG...')

    # check for established connection and join channels
    if (config.nick + " MODE " + config.nick) in data:
        s.send(irccommands.join(config.channel))

    # MESSAGE STRUCTURE
    # data.split()[0] = user
    # data.split()[1] = command
    # data.split()[2]  = channel
    # data.split()[3] = message

    try:
        msgcommand = data.split()[1]
    except:
        msgcommand = None

    # If the bot receives a PRIVMSG act accordingly
    if msgcommand == "PRIVMSG":
        msgnick = data.split()[0].split("!")[0][1:]
        msgchannel = data.split()[2]
        msg = data.split(":")[2:][0].replace(irccommands.CRLF, '')

        # # = administrative commands
        # $ = regular user commands
        if msg[0] == '#' or msg[0] == '$':
            #create queue for messages to the server
            queue = botcommands.process(msgnick, msgchannel, msg)
            #process queue
            for action in queue:
                s.send(action)

    # Print the received data
    # Useful for debugging or learning how IRC works
    print(data)
