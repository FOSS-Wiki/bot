import discord
from discord.ext import commands


class Help(commands.Cog):
    """Add help slash command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="help", description="Show help", aliases=["commands"])
    async def help(self, ctx: commands.Context, *, command_name: str = None):
        await ctx.defer(ephemeral=True)
        await ctx.invoke(self.bot.get_command("help"), command_name)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
