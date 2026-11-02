import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

class WikiBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="w$",
            intents=intents,
            help_command=None,
        )

    async def setup_hook(self):
        print("Setting up bot...")
        
        await self.load_extension("cogs.linker")

        await self.tree.sync()
        print("Command tree synced!")

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

async def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN is not set in your .env file. Exiting.")
        return

    bot = WikiBot()
    async with bot:
        await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
