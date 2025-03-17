import coc
from typing import Any


class ClashUtils:
    __slots__: tuple[str] = ("client",)

    # Donation Achievement names and multiplication factors
    DONATION_ACH: dict[str, int] = {
        "Friend in Need": 1,
        "Sharing is caring": 1,
        "Siege Sharer": 30,
    }

    COLORS: dict[str, int] = {
        "APPROVED": int(0xC1E1C1),
        "WARNING": int(0xFFFAA0),
        "REJECTED": int(0xFAA0A0),
    }

    DONATION_THRESHOLD: int = 25000
    TOWNHALL_THRESHOLD: int = 10

    def __init__(self, client: coc.EventsClient) -> None:
        self.client: coc.EventsClient = client

    @staticmethod
    def prep_tag(tag: str) -> str:
        return tag.strip().lstrip("#").upper()

    @classmethod
    def total_donations(cls, player: coc.Player) -> int:
        return sum(
            [
                player.get_achievement(achievement).value * factor
                for achievement, factor in cls.DONATION_ACH.items()
            ]
        )

    @classmethod
    def approval_color(cls, player: coc.Player) -> int:
        if player.town_hall >= cls.TOWNHALL_THRESHOLD:
            if cls.total_donations(player) >= cls.DONATION_THRESHOLD:
                return cls.COLORS["APPROVED"]
            return cls.COLORS["WARNING"]
        return cls.COLORS["REJECTED"]

    async def player_embed(self, tag: str) -> dict[str, Any] | None:
        tag: str = self.prep_tag(tag)
        try:
            player: coc.Player = await self.client.get_player(tag)
        except coc.NotFound:
            return None

        embed_dict: dict[str, Any] = {
            "title": player.name,
            "thumbnail": {"url": player.league.icon.url},
            "url": f"https://cc.fwafarm.com/cc_n/member.php?tag={tag}",
            "color": self.approval_color(player),
            "fields": [
                {"name": "TownHall", "value": player.town_hall},
                {"name": "Trophies", "value": player.trophies},
                {"name": "War Stars", "value": player.war_stars},
                {"name": "Donations", "value": self.total_donations(player)},
                {
                    "name": "Clan",
                    "value": player.clan.name
                    if player.clan is not None
                    else "`NO CLAN`",
                },
            ],
        }
        return embed_dict
