# IRC Commands
# IRC commands sent by the bot

CRLF = "\r\n"  # line terminator


#PONG
def pong(data):
    return 'PONG :' + data.split(":")[1].replace(CRLF, '') + CRLF


#NICK
def nick(nick):
    return 'NICK ' + nick + CRLF


#USER
def user(nick, server, realname):
    return 'USER ' + nick + ' ' + server + ' ' + nick + ' :' + realname + CRLF


#JOIN
def join(channel):
    return 'JOIN :' + channel + CRLF


#PRIVMSG
def privmsg(channel, message):
    return 'PRIVMSG ' + channel + ' :' + message + CRLF


#QUIT
def quit(message):
    return 'QUIT :' + message + CRLF