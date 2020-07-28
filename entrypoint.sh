#!/bin/sh
echo yes | git clone --depth 1 https://github.com/kittycloud/discord-bots.git -- kevin-the-cat.py
/usr/local/bin/python3 kevin-the-cat.py