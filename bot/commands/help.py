import discord
from discord.ext import commands


class Help(commands.Cog):
    """Add help slash command"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="help", description="Show help", aliases=["commands"])
    async def help(self, ctx: commands.Context, *, command_name: str = None):
        await ctx.defer(ephemeral=True)

        send_kwargs = {"ephemeral": True} if ctx.interaction else {}

        if command_name:
            command = self.bot.get_command(command_name)
            if command is None:
                await ctx.send(f"No command found for `{command_name}`.", **send_kwargs)
                return

            embed = discord.Embed(
                title=f"Command: {command.qualified_name}",
                color=discord.Color.blurple(),
                timestamp=discord.utils.utcnow(),
            )
            embed.add_field(
                name="Description",
                value=command.help or command.brief or "No description available.",
                inline=False,
            )
            signature = f"{ctx.clean_prefix}{command.qualified_name} {command.signature}".strip()
            embed.add_field(name="Usage", value=f"`{signature}`", inline=False)
            if command.aliases:
                embed.add_field(
                    name="Aliases",
                    value=", ".join(f"`{alias}`" for alias in command.aliases),
                    inline=False,
                )
            await ctx.send(embed=embed, **send_kwargs)
            return

        visible_commands = [
            cmd
            for cmd in self.bot.commands
            if not cmd.hidden and cmd.name != "help"
        ]
        visible_commands.sort(key=lambda cmd: cmd.name)

        description = "\n".join(
            f"`{ctx.clean_prefix}{cmd.name}` - {cmd.help or cmd.brief or 'No description available.'}"
            for cmd in visible_commands
        )
        if not description:
            description = "No commands are currently available."

        embed = discord.Embed(
            title="Available Commands",
            description=description,
            color=discord.Color.blurple(),
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(text=f"Use {ctx.clean_prefix}help <command> for details.")
        await ctx.send(embed=embed, **send_kwargs)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
