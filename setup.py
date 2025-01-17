import asyncio
import os

import mongoengine
from dotenv import find_dotenv, load_dotenv

from data.model.guild import Guild

load_dotenv(find_dotenv())

async def setup():
    print("STARTING SETUP...")
    guild = Guild()

    # you should have this setup in the .env file beforehand
    guild._id          = int(os.environ.get("MAIN_GUILD_ID"))

    # If you're re-running this script to update a value, set case_id
    # to the last unused case ID or else it will start over from 1!
    guild.case_id      = 1

    # required for permissions framework!
    guild.role_administrator = 927792962325315614  # put in the role IDs for your server here
    guild.role_moderator     = 927793486969831425  # put in the role IDs for your server here
    guild.role_birthday      = 1197157884329467924  # put in the role IDs for your server here
    guild.role_sub_mod       = 927794087971651656  # put in the role IDs for your server here
    guild.role_genius        = 927794087971651656  # put in the role IDs for your server here
    guild.role_dev           = 1197158964392120470  # put in the role IDs for your server here
    guild.role_memberone     = 1068519548933898261  # put in the role IDs for your server here
    guild.role_memberedition = 1068519606718832651  # put in the role IDs for your server here
    guild.role_memberpro     = 1068519090521657384  # put in the role IDs for your server here
    guild.role_memberplus    = 1068519004186091581  # put in the role IDs for your server here
    guild.role_memberultra   = 1068519463810506863  # put in the role IDs for your server here

    # not required if you don't want the /subnews command
    guild.role_sub_news      = 123  # put in the role IDs for your server here

    guild.channel_reports        = 123  # put in the channel IDs for your server here
    # channel where reactions will be logged
    guild.channel_emoji_log      = 123  # put in the channel IDs for your server here
    # channel for private mod logs
    guild.channel_private        = 123  # put in the channel IDs for your server here
    # channel where self-assignable roles will be posted
    guild.channel_reaction_roles = 123  # put in the channel IDs for your server here
    # rules-and-info channel
    guild.channel_rules          = 123  # put in the channel IDs for your server here
    # not required
    guild.channel_applenews      = 123  # put in the channel IDs for your server here
    # channel for public mod logs
    guild.channel_public         = 1146783412603080836 # put in the channel IDs for your server here
    # optional, used for /subnrews command or something
    guild.channel_subnews        = 123  # put in the channel IDs for your server here
    # optional, required for /issue command
    guild.channel_common_issues  = 123  # put in the channel IDs for your server here
    # #general, required for permissions
    guild.channel_general        = 918077533164032064 # put in the channel IDs for your server here
    # required for filter
    guild.channel_development    = 1197160519602282587  # put in the channel IDs for your server here
    # required, #bot-commands channel
    guild.channel_botspam        = 1146456071423152178  # put in the channel IDs for your server here
    # optional, needed for booster #emote-suggestions channel
    guild.channel_booster_emoji  = 123  # put in the channel IDs for your server here

    # you can fill these in if you want with IDs, or you ca use commands later
    guild.logging_excluded_channels = []  # put in a channel if you want (ignored in logging)
    guild.filter_excluded_channels  = []  # put in a channel if you want (ignored in filter)
    guild.filter_excluded_guilds    = []  # put guild ID to whitelist in invite filter if you want

    guild.nsa_guild_id = 123 # you can leave this as is if you don't want Blootooth (message mirroring system)

    guild.save()
    print("DONE")

if __name__ == "__main__":
    if os.environ.get("DB_CONNECTION_STRING") is None:
        mongoengine.register_connection(
            host=os.environ.get("DB_HOST"), port=int(os.environ.get("DB_PORT")), alias="default", name="botty")
    else:
        mongoengine.register_connection(
            host=os.environ.get("DB_CONNECTION_STRING"), alias="default", name="botty")
    res = asyncio.get_event_loop().run_until_complete( setup() )
