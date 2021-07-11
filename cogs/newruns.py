import json
from typing import Dict, List

import discord
from discord.ext import commands


class NewRuns(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def addgame(
        self, ctx: commands.Context, abbreviation: str, channel: discord.TextChannel
    ) -> None:
        """
        Add a new game
        """

        with open("gamedb.json") as f:
            gamedb = json.load(f)

        if ctx.guild.id not in gamedb:
            gamedb["guilds"][str(ctx.guild.id)] = {"games": []}

        # TODO: do stuff


def setup(bot: commands.Bot):
    bot.add_cog(NewRuns(bot))
