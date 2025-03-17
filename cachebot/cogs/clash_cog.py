import discord
import clash
from typing import Any


class ClashCog(discord.Cog):
    __slots__: tuple[str] = ("clash_util",)

    def __init__(self, clash_util: clash.ClashUtils) -> None:
        self.clash_util: clash.ClashUtils = clash_util

    # TODO: Remove Guild ID after release
    @discord.command(
        guild_ids=[1068210558362468482], description="Fetch Player Data"
    )
    async def fetch(
        self,
        ctx: discord.ApplicationContext,
        tag: discord.Option = discord.Option(str, "Player Tag", required=True),
    ) -> None:
        embed_dict: dict[str, Any] = await self.clash_util.player_embed(tag)
        if embed_dict is None:
            await ctx.respond("NOT FOUND!")
        else:
            embed: discord.Embed = discord.Embed.from_dict(embed_dict)
            await ctx.respond(embed=embed)
