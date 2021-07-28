import json
from typing import Dict

from discord.ext import commands


class GameList(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def get_game_by_id(self, id: str) -> Dict:
        async with self.bot.session.get(
            f"https://speedrun.com/api/v1/games/{id}"
        ) as res:
            return await res.json()

    async def get_game_by_abbr(self, abbreviation: str) -> Dict:
        async with self.bot.session.get(
            "https://speedrun.com/api/v1/games",
            params={"abbreviation": abbreviation},
        ) as res:
            return await res.json()

    @commands.command()
    async def addgame(self, ctx: commands.Context, abbreviation: str) -> None:
        """
        Add a new game
        """

        with open("gamedb.json", "r") as f:
            gamedb = json.load(f)

        # add this guild if it doesnt exist in the gamedb file yet
        if str(ctx.guild.id) not in gamedb["guilds"]:
            gamedb["guilds"][str(ctx.guild.id)] = {"games": []}

        data = await self.get_game_by_abbr(abbreviation)

        if "status" in data and "message" in data:
            status = data["status"]
            message = data["message"]
            raise RuntimeError(f"Error {status}: {message}")

        # if len(data["data"]) == 0, there is no game with this abbreviation
        if len(data["data"]) == 0:
            await self.bot.send_pretty(
                ctx,
                f"Error: could not find a game at https://speedrun.com/{abbreviation}",
            )
            return

        id = data["data"][0]["id"]
        name = data["data"][0]["names"]["international"]

        if id in gamedb["guilds"][str(ctx.guild.id)]["games"]:
            await self.bot.send_pretty(ctx, "Error: the game has already been added!")
            return

        # add the game to this guild's game list
        gamedb["guilds"][str(ctx.guild.id)]["games"].append(id)

        # write changes
        with open("gamedb.json", "w") as f:
            json.dump(gamedb, f, indent=4)

        await self.bot.send_pretty(ctx, f"Successfully added {name} to the game list!")

    @commands.command()
    async def removegame(self, ctx: commands.Context, abbreviation: str) -> None:
        """
        Remove a game
        """

        with open("gamedb.json", "r") as f:
            gamedb = json.load(f)

        # check if there are any games associated with this guild
        if (
            str(ctx.guild.id) not in gamedb["guilds"]
            or len(gamedb["guilds"][str(ctx.guild.id)]["games"]) == 0
        ):
            await self.bot.send_pretty(
                ctx,
                "Error: no games were added yet. use the `addgame` command to add some!",
            )
            return

        data = await self.get_game_by_abbr(abbreviation)

        if "status" in data and "message" in data:
            status = data["status"]
            message = data["message"]
            raise RuntimeError(f"Error {status}: {message}")

        # if len(data["data"]) == 0, there is no game with this abbreviation
        if len(data["data"]) == 0:
            await self.bot.send_pretty(
                ctx,
                f"Error: could not find a game at https://speedrun.com/{abbreviation}",
            )
            return

        id = data["data"][0]["id"]
        name = data["data"][0]["names"]["international"]

        # check if the game is actually added
        if id in gamedb["guilds"][str(ctx.guild.id)]["games"]:
            await self.bot.send_pretty(
                ctx,
                f"Error: {name} was not added. use the `addgame` command to add it!",
            )
            return

        # remove the game
        gamedb["guilds"][str(ctx.guild.id)]["games"].remove(id)

        await self.bot.send_pretty(
            ctx,
            f"Successfully removed {name} from the list!",
        )

        # write changes
        with open("gamedb.json", "w") as f:
            json.dump(gamedb, f, indent=4)


def setup(bot: commands.Bot):
    bot.add_cog(GameList(bot))
