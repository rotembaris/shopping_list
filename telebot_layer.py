import json
from telegram.ext import (
    Application,
    CommandHandler
)


from shopping_list_api import add_item, remove_item, welcome


async def send_welcome(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome())

async def bot_add_item(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=add_item(update.message.text))

async def bot_remove_item(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=remove_item(update.message.text))


def main():
    token = json.load(open("config.json"))["telegram_token"]
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", send_welcome))
    application.add_handler(CommandHandler("add_item", bot_add_item))
    application.add_handler(CommandHandler("remove_item", bot_remove_item))
    application.run_polling()
	
if __name__ == '__main__':
	main()
