import discord
from discord.ext import commands
import asyncio
import time


class Client:

    def __init__(self):
        self.discord_client = discord.Client()
        self.discord_bot = commands.Bot(command_prefix="!")

    def run_from_token_txt(self, path):
        token_file = open(path, 'r')
        token = token_file.readline().replace('\n', '')
        token_file.close()
        self.discord_bot.run(token)

    def set_channel_from_id(self, id):
        self.channel = self.discord_bot.get_channel(id)

    async def say(self, text):
        await self.discord_bot.send_message(self.channel, text)

    def on_message(self, function_):
        self.message_response = function_
        @self.discord_bot.event
        async def on_message(message):
            await self.message_response()
