import asyncio


async def get_new_runs(bot) -> None:
    async with bot.session.get(
        "https://www.speedrun.com/api/v1/runs?status=verified&orderby=verify-date&direction=desc"
    ) as response:
        runsdata = response.json()
        # TODO handle new runs

    await asyncio.sleep(300)
    await get_new_runs(bot)
