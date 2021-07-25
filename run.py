import asyncio
async def get_new_runs(bot) -> None:
    async with session.get('https://www.speedrun.com/api/v1/runs?status=verified&orderby=verify-date&direction=desc') as response:
        bot.logger.info("in get_new_runs")
        bot.logger.info(response)
    await asyncio.sleep(300)
    await get_new_runs(bot)
  
  