## Bot Commands
## Commands accepted by the bot

import irccommands
import config
import strings
from time import gmtime, strftime

strerrs = strings.errors[config.lang]
strmsgs = strings.messages[config.lang]

commands = {'auth': '#login',  # authenticate user
    'sendmsg': '#sendas',  # send message as bot
    'echo': '$echo',  # echo message
    'quit': '#quit',  # logout and terminate bot execution
    'msgdetails': '$msgdet'  # prints message info (debug)
    # 'loadmodule': '#load'  # loads a module
    # 'reloadmodule': '#reload'  # reloads a module
    # 'unloadmodule': '#unload'  # unloads a module
}


### Process commands
# Function used to process commands sent to the server
def process(msgnick, msgchannel, msg):

    # Create action queue
    queue = list()
    foundcommand = False

    # Run through available command list and see if one was called
    for i in commands:
        if msg.split(' ')[0] == commands[i]:
            restmsg = ' '.join(msg.split(' ')[1:])  # lint:ok

            #If there's nothing more in the message make it None
            if restmsg == '':
                restmsg = None

            #check if the message channel is the bot's nick to reply in private
            if msgchannel == config.nick:
                msgchannel = msgnick

            # run corresponding function
            queue = eval(i + '(msgnick, msgchannel, restmsg)')

            # let the program know the command was found
            foundcommand = True
            break

    # if the command was not found print error
    if not foundcommand:
        # error 0 command not exist
        action = strerrs[0]

        #check if the message channel is the bot's nick to reply in private
        if msgchannel == config.nick:
            msgchannel = msgnick

        # append to action queue
        action = irccommands.privmsg(msgchannel, action)

        queue.append(action)

    return queue


# print message details
def msgdetails(msgnick, msgchannel, msg):
    queue = list()

    currtime = strftime('%Y-%m-%d %H:%M:%S', gmtime())
    msgsz = str(len(msg))
    queue.append(irccommands.privmsg(msgchannel, strmsgs[3] + msgnick))
    queue.append(irccommands.privmsg(msgchannel, strmsgs[4] + msgchannel))
    queue.append(irccommands.privmsg(msgchannel, strmsgs[5] + msg))
    queue.append(irccommands.privmsg(msgchannel, strmsgs[6] + msgsz))
    queue.append(irccommands.privmsg(msgchannel, strmsgs[7] + currtime))

    return queue


### Authentication

## Check if user is authenticated
def authcheck(nick):

    isauth = False

    if nick in config.authenticated:
        isauth = True

    return isauth


## Authenticate user
def auth(msgnick, msgchannel, msg):

    queue = list()

    # Check if user is authenticating by private message
    # Since for private messages msgchannel was mapped to the user sending
    # the message we'll check if msgchannel and msgnick are the same
    if msgchannel != msgnick:

        # error 1 can only sign in by privaemsg
        errmsg = strerrs[1]
        queue.append(irccommands.privmsg(msgchannel, errmsg))
        return queue

    # Check if user has signed in
    if authcheck(msgnick):
        # error 2 already signed in
        errmsg = strerrs[2]
        queue.append(irccommands.privmsg(msgchannel, errmsg))
        return queue

    # Check if user is in bot masters list and check password
    if msg == config.password and msgnick in config.masters:

        config.authenticated.add(msgnick)
        # message 0 signed in
        errmsg = strmsgs[0]
        queue.append(irccommands.privmsg(msgchannel, errmsg))
        return queue

    # else = incorrect password
    else:
        # error 3 wrong user or passwd
        errmsg = strerrs[3]

        queue.append(irccommands.privmsg(msgchannel, errmsg))
        return queue


### Echo whatever the users say
def echo(msgnick, msgchannel, msg):

    queue = list()
    # user said: xyz...
    msg = msgnick + strmsgs[1] + msg
    queue.append(irccommands.privmsg(msgchannel, msg))
    return queue


### Quit: terminate bot execution
def quit(msgnick, msgchannel, msg=None):
    queue = list()

    if msg is None:
        msg = strmsgs[2]

    # Check if user has signed in and run command
    if authcheck(msgnick):
        queue.append(irccommands.privmsg(msgchannel, msg))
        queue.append(irccommands.quit(msg))
        return queue
    # Return error if user is not signed in
    else:
        errmsg = strerrs[4]
        queue.append(irccommands.privmsg(msgchannel, errmsg))
        return queue
