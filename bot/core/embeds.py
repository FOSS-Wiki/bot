"""Discord embed utilities for consistent styling."""

import discord
from typing import List, Optional, Tuple, Union


class EmbedColors:
    """Color constants for different embed types."""

    SUCCESS = 0x00FF00
    ERROR = 0xFF0000
    WARNING = 0xFFA500
    INFO = 0x0099FF
    PENDING = 0xFFFF00


class WikiEmbeds:
    """Standardized embeds for wiki bot functionality."""

    @staticmethod
    def success(
        title: str,
        description: str,
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create a success embed."""
        embed = discord.Embed(
            title=f"✅ {title}",
            description=description,
            color=EmbedColors.SUCCESS,
            timestamp=discord.utils.utcnow(),
        )
        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed

    @staticmethod
    def error(
        title: str,
        description: str,
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create an error embed."""
        embed = discord.Embed(
            title=f"❌ {title}",
            description=description,
            color=EmbedColors.ERROR,
            timestamp=discord.utils.utcnow(),
        )
        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed

    @staticmethod
    def warning(
        title: str,
        description: str,
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create a warning embed."""
        embed = discord.Embed(
            title=f"⚠️ {title}",
            description=description,
            color=EmbedColors.WARNING,
            timestamp=discord.utils.utcnow(),
        )
        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed

    @staticmethod
    def info(
        title: str,
        description: str,
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create an info embed."""
        embed = discord.Embed(
            title=f"ℹ️ {title}",
            description=description,
            color=EmbedColors.INFO,
            timestamp=discord.utils.utcnow(),
        )
        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed

    @staticmethod
    def pending(
        title: str,
        description: str,
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create a pending/in-progress embed."""
        embed = discord.Embed(
            title=f"📬 {title}",
            description=description,
            color=EmbedColors.PENDING,
            timestamp=discord.utils.utcnow(),
        )
        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed

    @staticmethod
    def verification_start(
        user: Union[discord.User, discord.Member], verification_url: str
    ) -> discord.Embed:
        """Create verification start embed."""
        embed = discord.Embed(
            title="🔗 MediaWiki Verification",
            description="**Click the link below to verify your MediaWiki account:**",
            color=EmbedColors.INFO,
            timestamp=discord.utils.utcnow(),
        )
        embed.add_field(
            name="🌐 Verify MediaWiki Account",
            value=(
                "🔒 **Do not share this link with anyone, including FOSS Wiki staff.**\n"
                f"\n**__{verification_url}__**\n"
            ),
            inline=False,
        )
        embed.add_field(
            name="What happens next:",
            value=(
                "1. You'll be redirected to the wiki's OAuth page\n"
                "2. Login with your MediaWiki account\n"
                "3. Authorize the bot to verify your identity\n"
                "4. If you meet the [requirements](https://foss.wiki/FW:Discord_Linking), you'll automatically receive the wiki editor role\n\n"
                "**⏰ Link expires in 10 minutes.**\n"
            ),
            inline=False,
        )
        embed.set_footer(
            text=f"Verification for {user.display_name}",
            icon_url=user.display_avatar.url,
        )
        embed.add_field(
            name="🔒 Security Note",
            value="This verification only grants us permission to see your username.",
            inline=False,
        )
        return embed

    @staticmethod
    def verification_complete(
        user: Union[discord.User, discord.Member], wiki_username: str
    ) -> discord.Embed:
        """Create verification complete embed."""
        embed = discord.Embed(
            title="✅ Verification Complete!",
            description=(
                f"Successfully linked **{user.display_name}** to MediaWiki account **{wiki_username}**.\n\n"
                "🎉 If you meet the requirement listed [here](https://foss.wiki/FW:Discord_Linking) you have been granted Wiki Author!\n"
                "📝 Thank you for contributing! You have gained access to VIP lounge and been granted extra permissions."
            ),
            color=EmbedColors.SUCCESS,
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(
            text=f"Welcome to the wiki, {wiki_username}!",
            icon_url=user.display_avatar.url,
        )
        return embed

    @staticmethod
    def verification_status(
        verified_users: List[Tuple[int, str]],
        user: Optional[Union[discord.User, discord.Member]] = None,
    ) -> discord.Embed:
        """Create verification status embed."""
        if not verified_users:
            embed = discord.Embed(
                title="📊 Verification Status",
                description="No verified users yet.",
                color=EmbedColors.INFO,
                timestamp=discord.utils.utcnow(),
            )
        else:
            user_list: List[str] = []
            for discord_id, wiki_username in verified_users[:10]:  # Limit to first 10
                user_list.append(f"• <@{discord_id}> → **{wiki_username}**")

            description = "\n".join(user_list)
            if len(verified_users) > 10:
                description += f"\n\n*... and {len(verified_users) - 10} more users*"

            embed = discord.Embed(
                title="📊 Verified Users",
                description=description,
                color=EmbedColors.SUCCESS,
                timestamp=discord.utils.utcnow(),
            )
            embed.add_field(
                name="📈 Total Verified",
                value=f"**{len(verified_users)}** users",
                inline=True,
            )

        if user:
            embed.set_footer(
                text=f"Requested by {user.display_name}",
                icon_url=user.display_avatar.url,
            )
        return embed
