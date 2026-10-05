import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Welcome! I'm J Bright Reply Bot.\n\nSend me a message and I'll reply."
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "🆘 Help\n\nSend me any message and I'll respond."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "👋 Thanks for your message! I'm J Bright Reply Bot."
    )

print("Bot is running...")
bot.infinity_polling()
