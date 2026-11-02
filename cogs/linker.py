from discord.ext import commands
import re

LINK_REGEX = re.compile(r"\[\[([^\n\[\]\\\s#<|{}_�:][^\n\[\]\\<|{}�]*?)\]\](?=([^`]|```([^`]|`{1,2}([^`]|$))+?```|``([^`]|`([^`]|$))+?``|`[^`]+?`)*$)")

# Automatically reply to a message with links to foss.wiki articles if it contains a properly formatted wikilink
class AutoLinker(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        matches = LINK_REGEX.findall(message.content)

        if (len(matches) == 0):
            return

        links = [f'[foss.wiki/{match[0]}](https://foss.wiki/{match[0].replace(" ", "_")})' for match in matches]

        await message.reply(content=', '.join(links))

async def setup(bot: commands.Bot):
    await bot.add_cog(AutoLinker(bot))
