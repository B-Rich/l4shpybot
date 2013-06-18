l4shpybot
=========

What is it?
-----------

*l4shpybot* is a very simple (for now) IRC bot I'm building for fun and as a learning experience.

How do I run it?
----------------

It has a config module (*config.py*) where you can put all the info the bot needs to connect, like server, server port, channel(s), nick(s) used by the bot, bot masters, etc.

After you have set what you need in *config.py* run *l4shbot.py*.

Use python:
```bash
python l4shbot.py
```
or set executable permissions and run it:
```bash
chmod +x l4shbot.py
./l4shbot.py
```

Connect to the server you configured and */query* the bot or join the channel you specified (default is *#bottest*)

License
-------

Except where otherwise noted the license this whole project is licensed under a zlib based license which explicitly states:

* You may freely study, modify and distribute.
* This software is free of charge and shall remain free.
* There's no warranty and the author(s) is/are **NOT** responsible for what you do with it or what it does to your system.
* You may use entirely or parts of it to develop free or commercial products as long as you credit the original author(s).
* You may sell products derived from this software as long as the parts used do not constitute over 50% of the new product.

For more information read LICENSE.txt

TO DO LIST (not ordered)
------------------------
* Module handling
* AI module
* SSL support
* *Help* command 
* <del>Basic connection</del>
* <del>Joining channels on login</del>
* <del>Bot master login</del>
* <del>*Quit* command</del>
