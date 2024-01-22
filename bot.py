config = {
    # Replace right-side with your emoji IDs
    'ShardRed_emoji':'<:ShardRed:1198069899973636137>',
    'ShardBlack_emoji':'<:ShardBlack:1198069944697503894>',
    'AscendedCandle_emoji':'<:AscendedCandle:1198069985017331852>'
}

import asyncio
import os
import pendulum
import discord 
import random
import aioduckdb
from discord.ext import commands,tasks
from discord import app_commands
from datetime import datetime,timedelta
from typing import Literal, Union, NamedTuple
import time

db_name = "data.db"
sky_bot_token = os.environ.get("sky_bot_token")

# Set up bot with '!' command prefix.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.tree.command(
    name="help",
    description="Learn how to use the bot to retrieve info about Sky"
)
async def help(interaction: discord.Interaction):
    help_text = """
# How to use the Sky Discord Bot 🌟

## Shard Functions 💎

- **/current_shard** 🌈
  - Get info about the current shard

- **/next_shards** 🔮
  - Retrieve details about upcoming shards.
    - Options:
      - `n`: Number of shards to predict.
      - `only`: Predict only Red or Black shards.

## Admin Functions 📡

- **/set_live_shard_channel** 📡
  - Set up a channel for live shard updates.
    - Required Parameter: Channel (discord.TextChannel).
    - Permissions: Administrator.

- **/remove_live_shard_channel** ❌
  - Remove live shard updates from the server.
    - Permissions: Administrator.

- **/set_daily_quest_channel** 🗓️
  - Set up a channel to be cleared daily.
    - Required Parameter: Channel (discord.TextChannel).
    - Permissions: Administrator.

## Virtual Hugs 🤗

- **/hug** 🤗
  - Send a virtual hug to another member.
    - Required Parameter: Member (discord.Member).
    - Permissions: Use Application Commands.

## Realm Functions 🏞️

Explore different realms with these commands:

- `/isle_of_dawn`
- `/daylight_prairie`
- `/hidden_forest`
- `/valley_of_triumph`
- `/golden_wasteland`
- `/vault_of_knowledge`
"""
    await interaction.response.send_message(help_text)

@bot.tree.command(
    name="hug",
    description="Virtual hugs"
)
@app_commands.checks.has_permissions(use_application_commands=True)
async def hug(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.defer(thinking = True)
    embed1 = discord.Embed(
        color = discord.Color.magenta()
    )
    embed1.set_author(
        name=f"{interaction.user.name} hugged {member.name}",
        icon_url=interaction.user.avatar)
    await interaction.followup.send(member.mention,embed = embed1,file=discord.File('public/emojis/icon_hug.webp', filename="map_image.webp"))

#####################################
# Isle of Dawn
#####################################
from src import realms

@bot.tree.command(
    name="isle_of_dawn",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Pointing Candlemaker",value="pointing_candlemaker"),
        app_commands.Choice(name="Rejecting Voyager",value="rejecting_voyager"),
        app_commands.Choice(name="Ushering Stargazer",value="ushering_stargazer")
    ]
)
async def isle_of_dawn(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "isle"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Daylight Prairie
#####################################


@bot.tree.command(
    name="daylight_prairie",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Applauding Bellmaker",value="applauding_bellmaker"),
        app_commands.Choice(name="Bird Whisperer",value="bird_whisperer"),
        app_commands.Choice(name="Butterfly Charmer",value="butterfly_charmer"),
        app_commands.Choice(name="Ceremonial Worshipper",value="ceremonial_worshipper"),
        app_commands.Choice(name="Exhausted Dock Worker",value="exhausted_dock_worker"),
        app_commands.Choice(name="Laughing Light Catcher",value="laughing_light_catcher"),
        app_commands.Choice(name="Slumbering Shipwright",value="slumbering_shipwright"),
        app_commands.Choice(name="Waving Bellmaker",value="waving_bellmaker"),
    ]
)
async def daylight_prairie(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "prairie"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Hidden Forest
#####################################
from src import realms

@bot.tree.command(
    name="hidden_forest",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Apologetic Lumberjack",value="apologetic_lumberjack"),
        app_commands.Choice(name="Blushing Prospector",value="blushing_prospector"),
        app_commands.Choice(name="Dismayed Hunter",value="dismayed_hunter"),
        app_commands.Choice(name="Hide'n'Seek Pioneer",value="hide_n_seek_pioneer"),
        app_commands.Choice(name="Shivering Trailblazer",value="shivering_trailblazer"),
        app_commands.Choice(name="Tearful Light Miner",value="tearful_light_miner"),
        app_commands.Choice(name="Whale Whisperer",value="whale_whisperer")
    ]
)
async def hidden_forest(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "forest"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Valley of Triumph
#####################################
from src import realms

@bot.tree.command(
    name="valley_of_triumph",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Backflipping Champion",value="backflipping_champion"),
        app_commands.Choice(name="Bowing Medalist",value="bowing_medalist"),
        app_commands.Choice(name="Cheerful Spectator",value="cheerful_spectator"),
        app_commands.Choice(name="Confident Sightseer",value="confident_sightseer"),
        app_commands.Choice(name="Handstanding Thrillseeker",value="handstanding_thrillseeker"),
        app_commands.Choice(name="Manta Whisperer",value="manta_whisperer"),
        app_commands.Choice(name="Proud Victor",value="proud_victor")
    ]
)
async def valley_of_triumph(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "valley"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Golden Wasteland
#####################################
from src import realms

@bot.tree.command(
    name="golden_wasteland",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Courageous Solider",value="courageous_soldier"),
        app_commands.Choice(name="Fainting Warrior",value="fainting_warrior"),
        app_commands.Choice(name="Frightened Refugee",value="frightened_refugee"),
        app_commands.Choice(name="Lookout Scout",value="lookout_scout"),
        app_commands.Choice(name="Saluting Captain",value="saluting_captain"),
        app_commands.Choice(name="Stealthy Survivor",value="stealthy_survivor")
    ]
)
async def golden_wasteland(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "wasteland"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Vault of Knowledge
#####################################
from src import realms

@bot.tree.command(
    name="vault_of_knowledge",
    description="Retrieve map and spirit info"
)
@app_commands.choices(
    map = [
        app_commands.Choice(name="Map Art",value="map_art"),
        app_commands.Choice(name="Map Pics",value="map_pic"),
    ],
    spirit = [
        app_commands.Choice(name="Trees",value="trees"),
        app_commands.Choice(name="Levitating Adept",value="levitating_adept"),
        app_commands.Choice(name="Meditating Monastic",value="meditating_monastic"),
        app_commands.Choice(name="Memory Whisperer",value="memory_whisperer"),
        app_commands.Choice(name="Polite Scholar",value="polite_scholar"),
        app_commands.Choice(name="Praying Acolyte",value="praying_acolyte")
    ]
)
async def vault_of_knowledge(interaction: discord.Interaction, map: app_commands.Choice[str] = None, spirit: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)
    realm = "vault"
    files_to_send,response = realms.get_files_to_send(realm,map,spirit)
    if len(files_to_send)>0:
        await interaction.followup.send(response,files=files_to_send)
    else:
        await interaction.followup.send("Sorry, something went wrong. Did you choose a map or spirit option?")

#####################################
# Shards
#####################################
from src import shardPredictor
async def get_shard_info_response(date=pendulum.now()):
    # Get today's date as string
    today_date_str = date
    # Get shard info for today
    shard_info = shardPredictor.get_shard_info(today_date_str)
    phase_status = shardPredictor.current_shard_status(today_date_str)
    # Image path
    map_image_path = f"public/infographics/map_clement/{shard_info['map']}.webp"
    eruptions = ",".join([f"<t:{int(x.timestamp())}:t>" for x in shard_info['eruptions']])
    
    # Customize the response based on the shard info
    if shard_info['haveShard']:
        if shard_info['isRed']:
            response = f"## {config['ShardRed_emoji']} **Red Shard Today:**\n"\
                       f"**Status: {phase_status['phase']} {phase_status['status']}**\n"\
                       f"Realm: {shard_info['RealmName']}\n"\
                       f"Map: {shard_info['MapName']}\n"\
                       f"Reward AC: {shard_info['rewardAC']} {config['AscendedCandle_emoji']}\n"\
                       f"Eruptions: {eruptions} \n"
        else:
            response = f"{config['ShardBlack_emoji']} **Black Shard Today:**\n"\
                       f"Realm: {shard_info['RealmName']}\n"\
                       f"Map: {shard_info['MapName']}\n"\
                       f"Eruptions: {eruptions}"
        return response, map_image_path
    else:
        return f"**No shard!**", 'public/noShard.gif'

@bot.tree.command(
    name='current_shard',
    description="Get information about Today's shard"
)
async def current_shard(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    # Get shard info and response
    response, map_image_path = await get_shard_info_response()
    # Post the shard of the day message
    await interaction.followup.send(response, file=discord.File(map_image_path, filename="map_image.webp"))

@bot.tree.command(
    name='next_shards',
    description="Retrieve the next few shards"
)
@app_commands.choices(
    only =[
        app_commands.Choice(name="Red Shards",value="red"),
        app_commands.Choice(name="Black Shards",value="black")]
)
async def next_shards(interaction: discord.Interaction,n: int = 5,  only: app_commands.Choice[str] = None):
    await interaction.response.defer(thinking=True)

    # Get today's date as string
    today_date_str = datetime.utcnow()

    # Get shard info for the next 5 shards
    if only:
        next_shards_info = shardPredictor.find_next_n_shards(n,{'only':only.value})
    else:
        next_shards_info = shardPredictor.find_next_n_shards(n)

    # Format occurrences for each shard
    formatted_shards = []
    for shard_info in next_shards_info:
        eruptions = ",".join([f"<t:{int((x + timedelta(minutes=8)).timestamp())}:t>" for x in shard_info['occurrences']])
        formatted_shards.append(
            f"""**{config['ShardRed_emoji'] + "Red" if shard_info['isRed'] == 1 else config['ShardBlack_emoji'] + "Black"} shard on <t:{int(shard_info['date'].timestamp())}:D> in {shard_info['MapName']},{shard_info['RealmName']}** \n \t {config['AscendedCandle_emoji'] if shard_info['isRed']==1 else ''} {eruptions}"""
        )

    # Combine the formatted shards into a single response
    response = f"## Today is <t:{int(datetime.now().timestamp())}:D>\n"+ "\n\n".join(formatted_shards)

    await interaction.followup.send(response)

@tasks.loop(minutes=3)  # Update every 3 minutes (adjust as needed)
async def post_live_shard_updates():
    async with aioduckdb.connect(db_name) as connection:
        async with connection.cursor() as cursor:
            # Check if the table exists
            await cursor.execute(
                """
                SELECT EXISTS (
                    SELECT 1 FROM information_schema.tables 
                    WHERE table_name = 'live_shard_channel'
                ) as table_exists
                """
            )
            table_exists_result = await cursor.fetchone()
            table_exists = table_exists_result[0]

            if table_exists:
                # Fetch data from the table
                await cursor.execute(
                    "SELECT guild_id, channel_id, message_id FROM live_shard_channel"
                )
                results = await cursor.fetchall()
                
                for result in results:
                    guild_id, channel_id, message_id = result
                    guild = bot.get_guild(guild_id)
                    channel = guild.get_channel(channel_id) if guild else None
                    if channel:
                        response, map_image_path = await get_shard_info_response()
                        # Try to get the existing message
                        existing_message = None
                        try:
                            existing_message = await channel.fetch_message(message_id)
                        except discord.NotFound:
                            pass

                        if existing_message:
                            await existing_message.edit(content="**Live Updates:** \n" + response, attachments=[discord.File(map_image_path, filename="map_image.webp")])
                        else:
                            new_message = await channel.send(response, file=discord.File(map_image_path, filename="map_image.webp"))
                            # Update the message_id in the database
                            await cursor.execute(
                                "UPDATE live_shard_channel SET message_id = ? WHERE guild_id = ? AND channel_id = ?",
                                (new_message.id, guild_id, channel_id),
                            )
                    else:
                        response = f"No Shard!"
                        # Try to get the existing message
                        existing_message = None
                        try:
                            existing_message = await channel.fetch_message(message_id)
                        except discord.NotFound:
                            pass

                        if existing_message:
                            await existing_message.edit(content="**Live Updates:** \n" + response, attachments=[discord.File('public/noShard.gif', filename="map_image.webp")])
                        else:
                            new_message = await channel.send("**Live Updates:** \n" + response, file=discord.File('public/noShard.gif', filename="map_image.webp"))
                            # Update the message_id in the database
                            await cursor.execute(
                                "UPDATE live_shard_channel SET message_id = ? WHERE guild_id = ? AND channel_id = ?",
                                (new_message.id, guild_id, channel_id),
                            )
            else:
                print("live_shard_channel table does not exist yet. Skipping update.")

#####################################
# Administrative stuff
#####################################
@bot.tree.command(
    name="set_live_shard_channel",
    description="Set up the channel for live shard updates."
)
@app_commands.checks.has_permissions(administrator=True)
async def set_live_shard_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    await interaction.response.defer(thinking=True)
    async with aioduckdb.connect(db_name) as connection:
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS live_shard_channel (
                guild_id BIGINT,
                channel_id BIGINT,
                message_id BIGINT
            )
            """
        )
        # Post the initial message and store the message_id in the database

        response, map_image_path = await get_shard_info_response()
        await interaction.followup.send(f"Live Shard Updates set for `#{channel.name}`")
        message = await channel.send("**Live Updates:** \n" + response,file=discord.File(map_image_path, filename="map_image.webp"))
        async with aioduckdb.connect(db_name) as connection:
            await connection.execute(
                "INSERT INTO live_shard_channel (guild_id, channel_id,message_id) VALUES (?, ?,?)",
                (interaction.guild_id, channel.id,message.id),
            )

@bot.tree.command(
    name="remove_live_shard_channel",
    description="Remove all live shard updates from the server."
)
@app_commands.checks.has_permissions(administrator=True)
async def remove_live_shard_channel(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    
    async with aioduckdb.connect(db_name) as connection:
        # Check if the guild has a live shard channel set up
        result = await connection.execute(
            "SELECT * FROM live_shard_channel WHERE guild_id = ?",
            (interaction.guild_id,),
        )
        row = await result.fetchone()
        
        if row:
            # If there is a record, remove the channel from the database
            await connection.execute(
                "DELETE FROM live_shard_channel WHERE guild_id = ?",
                (interaction.guild_id,),
            )
            
            await interaction.followup.send("Live shard channel removed successfully.")
        else:
            await interaction.followup.send("No live shard channel set up for this guild.")


@bot.tree.command(
    name="set_daily_quest_channel",
    description="Set up a channel to be cleared before daily resets"
)
@app_commands.checks.has_permissions(administrator=True)
async def set_daily_quest_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    await interaction.response.defer(thinking=True)
    shard_info = getattr(bot, 'shard_info', None)
    async with aioduckdb.connect(db_name) as connection:
        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_quest_channel (
                guild_id BIGINT,
                channel_id BIGINT
            )
            """
        )
        await connection.execute(
            "INSERT INTO daily_quest_channel (guild_id, channel_id) VALUES (?, ?)",
            (interaction.guild_id, channel.id),
        )
    await interaction.followup.send(f"Daily quest channel set to {channel.name}.")
    
clear_daily_quest_channel_running = False
@tasks.loop(minutes=1)
async def clear_daily_quest_channel(bot):
    global clear_daily_quest_channel_running
    
    clear_daily_quest_channel_running = True
    
    now = datetime.now(pendulum.timezone('America/Los_Angeles'))  # Set to Pacific Time Zone
    if now.hour == 23 and now.minute == 58:
        try:
            # Iterate over all guilds
            for guild in bot.guilds:
                your_guild_id = guild.id
                
                # Check if the table exists and a channel has been set
                async with aioduckdb.connect(db_name) as connection:
                    async with connection.cursor() as cursor:
                        await cursor.execute(
                            "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'daily_quest_channel') as table_exists"
                        )
                        table_exists_result = await cursor.fetchone()
                        table_exists = table_exists_result[0]
                        if table_exists:
                            await cursor.execute(
                                "SELECT channel_id FROM daily_quest_channel WHERE guild_id = ?",
                                (your_guild_id,),
                            )
                            channel_result = await cursor.fetchone()

                        elif not table_exists:
                            print(f"Daily quest channel table does not exist. Skipping.")
                            return

                # Retrieve channel ID from the database based on the guild ID
                async with aioduckdb.connect(db_name) as connection:
                    async with connection.cursor() as cursor:
                        await cursor.execute(
                            "SELECT distinct guild_id, channel_id FROM daily_quest_channel WHERE guild_id = ?",
                            (your_guild_id,),
                        )
                        results = await cursor.fetchall()

                        for result in results:
                            channel_id = result[1]
                            channel = bot.get_channel(channel_id)

                            if channel:
                                await channel.purge(limit=2000)
                                print(f"Daily quest channel for guild {your_guild_id} cleared.")
                            else:
                                print(f"Daily quest channel for guild {your_guild_id} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            clear_daily_quest_channel_running = False

@bot.tree.command(
    name="purge_messages",
    description="Purge the last n messages from a specific channel. (default n=100)"
)
@app_commands.checks.has_permissions(administrator=True)
async def purge_messages(interaction: discord.Interaction, channel: Union[discord.VoiceChannel, discord.TextChannel], n: int = 100):
    await interaction.response.send_message("Purging...")
    time.sleep(5)
    await channel.purge(limit=n)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    if not clear_daily_quest_channel_running:
        clear_daily_quest_channel.start(bot)
        
    #update_shard_info.start()
    post_live_shard_updates.start()
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)

bot.run(sky_bot_token)