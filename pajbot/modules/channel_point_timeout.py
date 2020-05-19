import logging
from datetime import timedelta

from pajbot.managers.handler import HandlerManager
from pajbot.managers.db import DBManager
from pajbot.modules import BaseModule
from pajbot.modules import ModuleSetting
from pajbot.models.user import User
from pajbot import utils

log = logging.getLogger(__name__)


class ChannelPointTimeout(BaseModule):
    ID = __name__.split(".")[-1]
    NAME = "Channel Point Timeout"
    DESCRIPTION = "Timeout people with channel points"
    CATEGORY = "Feature"
    SETTINGS = [
        ModuleSetting(
            key="redeemed_id_timeout",
            label="ID of redemeed prize for timeout",
            type="text",
            required=True,
            default="",
            constraints={"min_str_len": 36, "max_str_len": 36},
        ),
        ModuleSetting(
            key="redeemed_id_untimeout",
            label="ID of redemeed prize for untimeout",
            type="text",
            required=True,
            default="",
            constraints={"min_str_len": 36, "max_str_len": 36},
        ),
        ModuleSetting(key="timeout_duration", label="Duration in seconds for the timeout", type="number", required=True, default=3600),
    ]

    def __init__(self, bot):
        super().__init__(bot)
        self.user_list = {}
        # {
        #     "user_id": timeout_expiry_date_time
        # }

    def on_redeem(self, redeemer, redeemed_id, user_input):
        if user_input is not None:
            username = user_input.split()[0]
            if redeemed_id not in [self.settings["redeemed_id_timeout"], self.settings["redeemed_id_untimeout"]]:
                return

            with DBManager.create_session_scope() as db_session:
                user = User.find_by_user_input(db_session, username)
                if not user:
                    self.bot.whisper(redeemer, f"{username} has never typed in the chat.")
                    return

                if user.level >= 500 or user.moderator:
                    self.bot.whisper(redeemer, f"You cannout timeout moderators!")
                    return

                str_user_id = str(user.id)

                if redeemed_id == self.settings["redeemed_id_timeout"]:
                    duration = self.settings["timeout_duration"]
                    self.user_list[str_user_id] = utils.now() + timedelta(seconds=duration)
                    self.bot.timeout(user, duration, f"{redeemer.name} paid for their timeout")
                    self.bot.whisper(redeemer, f"Timedout {user.name} for {duration} seconds")
                    return

                if str_user_id not in self.user_list or self.user_list[str_user_id] < utils.now():
                    self.bot.whisper(redeemer, f"You can only untimeout people who have been timedout by this module.")
                    if str_user_id in self.user_list:
                        del self.user_list[str_user_id]
                    return

                self.bot.untimeout(user)
                self.bot.whisper(redeemer, f"Successfully untimed-out {user.name}")
                del self.user_list[str_user_id]

    def enable(self, bot):
        if not bot:
            return

        HandlerManager.add_handler("on_redeem", self.on_redeem)

    def disable(self, bot):
        if not bot:
            return

        HandlerManager.remove_handler("on_redeem", self.on_redeem)
