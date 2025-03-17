import discord
import asyncio
import coc
import clash
import tomllib
import cogs
from typing import Any


def main() -> None:
    bot: discord.Bot = discord.Bot()
    coc_client: coc.EventsClient = coc.EventsClient()
    clash_util: clash.ClashUtils = clash.ClashUtils(coc_client)

    with open("secrets.toml", "rb") as secrets_fp:
        secrets: dict[str, Any] = tomllib.load(secrets_fp)

    asyncio.get_event_loop().run_until_complete(
        coc_client.login(
            secrets["clash"]["email"], secrets["clash"]["password"]
        )
    )
    bot.add_cog(cogs.ClashCog(clash_util))
    bot.add_cog(cogs.EventsCog())

    bot.run(secrets["discord"]["token"])


if __name__ == "__main__":
    main()
