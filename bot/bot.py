#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import random


class Bot:
    """Bot template"""

    def __init__(self):
        self.token = "5101813342:AAHAB9Tz4h86P-ywf61237Cjsj7ZRhyt4ag"
        self.status = "resting"
        print("Initializing Bot...")

    def duel(self, update, context):
        """Response on /duel command from chat."""
        self.status = "fighting"
        msg = "Standard Battle Scream!"
        update.message.reply_text(msg)

    def read_chat(self, update, context):
        """Reads the chat messages."""
        while self.status == "fighting":
            user = update.message.from_user.username
            text = update.message.text
            print("[" + user + "] " + text)

            some_fancy_conditon = "creative stuff" == "creative stuff"

            if some_fancy_conditon:
                print("Condition meet!")

                update.message.reply_text(self.process(text))

            self.status = "resting"

    def process(self, text):
        print("Processing: " + text)
        return random()
