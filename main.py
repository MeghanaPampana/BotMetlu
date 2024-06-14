# main.py
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, member_counters

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, command: str, sender, mentioned_name, mentioned_display_name: str = None, value: int = 1) -> None:
    if not command:
        print('Empty command')
        return 

    try:
        response: str = get_response(command, sender, mentioned_name, mentioned_display_name, value)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    user_message: str = message.content
    mentioned_display_name = None
    mentioned_name = None
    command = None
    value = 1

    if message.mentions:
        parts = user_message.split()
        mentioned_display_name = message.mentions[0].display_name
        mentioned_name = message.mentions[0].name
        command = parts[0]
        if len(parts) > 2:
            try:
                value = int(parts[2])
            except ValueError:
                pass
    else:
        command = user_message.split()[0]

    # print(f"Command: {command}, Mentioned Member: {mentioned_display_name}, Value: {value}")
    # print(f'{message.author.name}')
    await send_message(message, command, message.author, mentioned_name, mentioned_display_name, value)

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
