from pajbot.modules.base import BaseModule
from pajbot.modules.base import ModuleSetting
from pajbot.modules.base import ModuleType
from pajbot.modules.linkchecker import BlacklistedLink
from pajbot.modules.linkchecker import WhitelistedLink
from pajbot.modules.linktracker import LinkTrackerLink


from pajbot.modules.analogy import AnalogyModule
from pajbot.modules.ascii import AsciiProtectionModule
from pajbot.modules.banphrase import BanphraseModule
from pajbot.modules.basic import BasicCommandsModule
from pajbot.modules.basic.ab import AbCommandModule
from pajbot.modules.basic.admincommands import AdminCommandsModule
from pajbot.modules.basic.checkmod import CheckModModule
from pajbot.modules.basic.dbmanage import DBManageModule
from pajbot.modules.basic.debug import DebugModule
from pajbot.modules.basic.emotes import EmotesModule
from pajbot.modules.basic.ignore import IgnoreModule
from pajbot.modules.basic.permaban import PermabanModule
from pajbot.modules.basic.pointsreset import PointsResetModule
from pajbot.modules.basic.stream_update import StreamUpdateModule
from pajbot.modules.bingo import BingoModule
from pajbot.modules.casechecker import CaseCheckerModule
from pajbot.modules.chat_alerts import ChatAlertModule
from pajbot.modules.chat_alerts.subalert import SubAlertModule
from pajbot.modules.chat_alerts.raidalert import RaidAlertModule
from pajbot.modules.chatters_refresh import Loyalty
from pajbot.modules.deck import DeckModule
from pajbot.modules.dubtrack import DubtrackModule
from pajbot.modules.duel import DuelModule
from pajbot.modules.dummy import DummyModule
from pajbot.modules.eightball import EightBallModule
from pajbot.modules.emote_timeout import EmoteTimeoutModule
from pajbot.modules.emotecombo import EmoteComboModule
from pajbot.modules.followage import FollowAgeModule
from pajbot.modules.givepoints import GivePointsModule
from pajbot.modules.lastfm import LastfmModule
from pajbot.modules.linefarming import LineFarmingModule
from pajbot.modules.linkchecker import LinkCheckerModule
from pajbot.modules.linktracker import LinkTrackerModule
from pajbot.modules.math import MathModule
from pajbot.modules.maxmsglength import MaxMsgLengthModule
from pajbot.modules.casechecker import CaseCheckerModule
from pajbot.modules.moderators_refresh import ModeratorsRefreshModule
from pajbot.modules.songrequest import SongrequestModule
from pajbot.modules.pointlottery import PointLotteryModule
from pajbot.modules.pyramid import PyramidModule
from pajbot.modules.quest import QuestModule
from pajbot.modules.quests.gettimedout import GetTimedOutQuestModule
from pajbot.modules.quests.typeemote import TypeEmoteQuestModule
from pajbot.modules.quests.typememessage import TypeMeMessageQuestModule
from pajbot.modules.quests.winduelpoints import WinDuelPointsQuestModule
from pajbot.modules.quests.winduels import WinDuelsQuestModule
from pajbot.modules.quests.winraffle import WinRaffleQuestModule
from pajbot.modules.raffle import RaffleModule
from pajbot.modules.repspam import RepspamModule
from pajbot.modules.roulette import RouletteModule
from pajbot.modules.slotmachine import SlotMachineModule
from pajbot.modules.subalert import SubAlertModule
from pajbot.modules.playsound import PlaysoundModule
from pajbot.modules.showemote import ShowEmoteModule
from pajbot.modules.subscriber_fetch import SubscriberFetchModule
from pajbot.modules.top import TopModule
from pajbot.modules.trivia import TriviaModule
from pajbot.modules.vanish import VanishModule
from pajbot.modules.warning import WarningModule
from pajbot.modules.massping import MassPingProtectionModule
from pajbot.modules.wolfram import WolframModule
from pajbot.modules.bet import BetModule
from pajbot.modules.spotify_streamlabs import SpotifyStreamLabs
from pajbot.modules.pnsl import PNSLModule
from pajbot.modules.spotifyquery import SpotifySongQuery
from pajbot.modules.reward_tts_amazon import RewardTTSModuleAmazon
from pajbot.modules.reward_tts_streamlabs import RewardTTSModuleStreamLabs
from pajbot.modules.convert_points import ConvertPoints
from pajbot.modules.paidtimeout import PaidTimeoutModule
from pajbot.modules.random_redeem_points import RandomRedeem
from pajbot.modules.taxation import Taxation
from pajbot.modules.emote_limit import EmoteLimitModule
from pajbot.modules.channel_point_timeout import ChannelPointTimeout


available_modules = [
    AnalogyModule,
    AbCommandModule,
    AdminCommandsModule,
    AsciiProtectionModule,
    BanphraseModule,
    BasicCommandsModule,
    BetModule,
    BingoModule,
    CaseCheckerModule,
    ChatAlertModule,
    Loyalty,
    ChannelPointTimeout,
    CheckModModule,
    ConvertPoints,
    DBManageModule,
    DebugModule,
    DubtrackModule,
    DuelModule,
    DummyModule,
    EightBallModule,
    EmoteComboModule,
    EmoteLimitModule,
    EmotesModule,
    EmoteTimeoutModule,
    FollowAgeModule,
    GetTimedOutQuestModule,
    GivePointsModule,
    IgnoreModule,
    LastfmModule,
    LineFarmingModule,
    LinkCheckerModule,
    LinkTrackerModule,
    Loyalty,
    MassPingProtectionModule,
    MathModule,
    MaxMsgLengthModule,
    ModeratorsRefreshModule,
    PaidTimeoutModule,
    PermabanModule,
    PlaysoundModule,
    PointLotteryModule,
    PointsResetModule,
    PyramidModule,
    QuestModule,
    RaffleModule,
    RaidAlertModule,
    RandomRedeem,
    RepspamModule,
    RewardTTSModuleAmazon,
    RewardTTSModuleStreamLabs,
    RouletteModule,
    ShowEmoteModule,
    SlotMachineModule,
    SongrequestModule,
    SpotifyStreamLabs,
    SpotifySongQuery,
    StreamUpdateModule,
    SubAlertModule,
    SubscriberFetchModule,
    Taxation,
    TopModule,
    TriviaModule,
    TypeEmoteQuestModule,
    TypeMeMessageQuestModule,
    VanishModule,
    WarningModule,
    WinDuelPointsQuestModule,
    WinDuelsQuestModule,
    WinRaffleQuestModule,
    WolframModule,
    PNSLModule,
]
