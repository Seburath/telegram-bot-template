#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bot template for the first anprog practice.
"""

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from .bot import Bot


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot = Bot()

    updater = Updater(bot.token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("duel", bot.duel))
    dp.add_handler(CommandHandler("d", bot.duel))

    dp.add_handler(MessageHandler(Filters.text, bot.read_chat))

    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == "__main__":
    main()
