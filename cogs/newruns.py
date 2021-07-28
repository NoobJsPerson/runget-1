import asyncio

from discord.ext import commands


class NewRuns(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def get_new_runs(self) -> None:
        async with self.bot.session.get(
            "https://www.speedrun.com/api/v1/runs",
            params={
                "status": "verified",
                "orderby": "verify-date",
                "direction": "desc",
            },
        ) as response:
            runsdata = response.json()
            # TODO handle new runs

        await asyncio.sleep(300)
        await self.get_new_runs()


def setup(bot: commands.Bot):
    bot.add_cog(NewRuns(bot))
