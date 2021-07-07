import os
import traceback

import discord
import git
from discord.ext import commands


class ExceptionHandler(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.ignored = (commands.CommandNotFound,)

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, exception: Exception
    ) -> None:
        if type(exception) in self.ignored:
            return

        elif isinstance(exception, commands.CommandOnCooldown):
            cooldown_retry = round(exception.retry_after, 1)

            cooldown_rate = exception.cooldown.rate
            cooldown_per = exception.cooldown.per
            cooldown_type = str(exception.cooldown.type).rsplit(".", 1)[-1]

            await self.bot.send_pretty(
                ctx,
                (
                    f"{ctx.author.mention}, you have to wait {cooldown_retry} seconds before using this again.\n"
                    f"The cooldown for this command is {cooldown_rate} per {cooldown_per}s for every {cooldown_type}"
                ),
            )
            return
        elif isinstance(exception, commands.CommandInvokeError):
            await self.bot.send_pretty(
                ctx,
                (
                    f"An exception occured while running this command.\n"
                    f"```python\n{''.join(traceback.format_exception(None, exception, exception.__traceback__))}\n```"
                ),
            )
            self.bot.logger.exception(exception)
        elif isinstance(exception, commands.CommandError):
            await self.bot.send_pretty(ctx, f"```\n{exception}\n```")
        elif isinstance(exception, discord.DiscordException):
            self.bot.logger.exception(exception)


def setup(bot: commands.Bot):
    bot.add_cog(ExceptionHandler(bot))
