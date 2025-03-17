import discord
from datetime import datetime, timezone


class EventsCog(discord.Cog):
    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print(f"READY! AT {datetime.now(timezone.utc).isoformat()} UTC")
