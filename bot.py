import datetime
import json
import logging
from typing import List

import aiohttp
import discord
from run import get_new_runs
from discord.ext import commands, tasks


extensions = ["cogs.admin", "cogs.exceptionhandler", "cogs.gamelist"]


def get_prefix(bot: commands.Bot, message: discord.Message) -> List[str]:
    return commands.when_mentioned_or(*bot.settings["prefixes"])(bot, message)


class SrcBot(commands.Bot):
    def __init__(self) -> None:
        with open("config.json", "r") as f:
            self.config = json.load(f)

        with open("settings.json", "r") as f:
            self.settings = json.load(f)

        activity = discord.Activity(
            name=f"for new runs | {self.settings['prefixes'][0]}help",
            type=discord.ActivityType.watching,
        )

        super().__init__(
            command_prefix=get_prefix,
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions(
                everyone=False, roles=False, users=True
            ),
            intents=discord.Intents.all(),
            activity=activity,
            status=discord.Status.online,
        )
        self.oldruns = {}
        self.logger = logging.getLogger("discord")
        self.session = aiohttp.ClientSession()

    async def on_ready(self) -> None:
        if not hasattr(self, "uptime"):
            self.uptime = datetime.datetime.utcnow()

        self.logger.info(
            f"running as {self.user} (id = {self.user.id}), "
            f"on {discord.__name__} v{discord.__version__}"
        )
        
    @tasks.loop(minutes=2.0)
    async def wrapper(self)
        await get_new_runs(self)

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        await self.process_commands(message)

    def run(self) -> None:
        for extension in extensions:
            self.load_extension(extension)
            self.logger.info(f"loaded extension {extension}")

        super().run(self.config["token"], reconnect=True)

    async def send_pretty(self, ctx: commands.Context, content: str) -> discord.Message:
        embed = discord.Embed(description=content)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url
        )
        embed.timestamp = ctx.message.created_at
        return await ctx.send(embed=embed)
