"""Configuration management for the Discord bot."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Bot configuration settings."""

    # Discord settings
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    DISCORD_PREFIX = os.getenv("DISCORD_PREFIX", "$w")

    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL")

    # MediaWiki settings
    VERIFICATION_URL = os.getenv("VERIFICATION_URL")
    MW_API_URL = os.getenv("MW_API_URL")

    # Role settings
    # Role settings
    # Safely parse optional integer env vars — guard against empty strings
    _wiki_role_raw = os.getenv("WIKI_AUTHOR_ROLE_ID", "")
    try:
        WIKI_AUTHOR_ROLE_ID = int(_wiki_role_raw) if _wiki_role_raw and _wiki_role_raw.strip() != "" else 0
    except (TypeError, ValueError):
        WIKI_AUTHOR_ROLE_ID = 0

    # Bot admin role IDs (not Discord admin permissions) - users with these roles can use admin commands
    _allowed_raw = os.getenv("ALLOWED_ROLE_IDS", "")
    if _allowed_raw and _allowed_raw.strip() != "":
        ALLOWED_ROLE_IDS = []
        for _part in _allowed_raw.split(","):
            _p = _part.strip()
            if not _p:
                continue
            try:
                ALLOWED_ROLE_IDS.append(int(_p))
            except ValueError:
                # ignore invalid entries
                continue
    else:
        ALLOWED_ROLE_IDS = []

    # Task intervals (in minutes)
    PURGE_INTERVAL = 30
    ROLE_GRANT_INTERVAL = 5

    # Token expiry (in hours)
    TOKEN_EXPIRY_HOURS = 3

    ENABLE_DB = False
    ENABLE_VERIFICATION = False
    ENABLE_AUTOLINKER = True
    ENABLE_API = False

    @classmethod
    def validate(cls) -> None:
        """Validate that required environment variables are set."""
        required_vars = [("DISCORD_TOKEN", cls.DISCORD_TOKEN)]

        # Database only required if DB is enabled
        if cls.ENABLE_DB:
            required_vars.append(("DATABASE_URL", cls.DATABASE_URL))

        # Verification and MW API only required if verification features are enabled
        if cls.ENABLE_VERIFICATION:
            required_vars.append(("VERIFICATION_URL", cls.VERIFICATION_URL))
            required_vars.append(("MW_API_URL", cls.MW_API_URL))

        missing_vars = [name for name, value in required_vars if not value]

        if missing_vars:
            raise RuntimeError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )

        assert cls.DISCORD_TOKEN is not None
