from telethon.sync import TelegramClient
from telethon.tl import functions

api_id = 'api_id '
api_hash = 'api_hash'
bot_token = 'bot_token'
receiver_username = 'r1eda'  # أو يمكنك استخدام ID أو رقم الهاتف هنا
message = 'اكتب رسالتك هنا'
num_messages = 10  # عدد الرسائل التي ترغب في إرسالها

# تكوين العميل
client = TelegramClient('bot_session', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    
    # ارسال الرسائل
    for _ in range(num_messages):
        await client.send_message(receiver_username, message)

    await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
