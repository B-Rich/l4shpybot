# Configuration module for l4shpybot
#
# server = server to connect to
# port = (int) server port
# channels = (list) channels that the bot will join #TO DO
# nicks = (list) nicks used by the bot  #TO DO
# nick = (str) nick the bot will use
# realname = (str) full name of the bot
# masters = (set) nicks allowed to authenticate and control the bot
# password = (str) password to authenticate the master
# lang = (str) language used by the bot, check strings.py

server = 'example.com'
port = 6667
channels = ['#bottest', '#bottest2']
channel = channels[0]
nicks = ['l4shpybot', 'lashpybot', 'botty', 'dummybot', 'dumbbot']
nick = nicks[3]
realname = 'Dumb Bot'  # When it develops intelligence it will be a smart bot ;)
masters = {'l4sh'}
password = '12345'
authenticated = set()
lang = 'en'
