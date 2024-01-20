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

db_name = "data.db"
sky_bot_token = os.environ.get("sky_bot_token")

# Set up bot with '!' command prefix.
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.tree.command(name="hug")
@app_commands.checks.has_permissions(use_application_commands=True)
async def hug(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.defer(thinking = True)
    embed1 = discord.Embed(
        color = discord.Color.purple()
    )
    embed1.set_author(
        name=f"{interaction.user.name} hugged {member.name}",
        icon_url=interaction.user.avatar)
    await interaction.followup.send(embed = embed1,file=discord.File('public/emojis/icon_hug.webp', filename="map_image.webp"))

from src import shardPredictor

@bot.tree.command(name='shard_of_the_day')
async def shard_of_the_day(interaction: discord.Interaction):
    await interaction.response.defer(thinking = True)
    
    # Get today's date as string
    today_date_str = datetime.utcnow()
    # Get shard info for today
    shard_info = shardPredictor.get_shard_info(today_date_str)
    
    # Image path
    map_image_path = f"public/infographics/map_clement/{shard_info['map']}.webp"
    occurrences = ",".join([f"<t:{int(x.timestamp())}:t>" for x in shard_info['occurrences']])
    # You can customize the response based on the shard info
    if shard_info['haveShard']:
        if shard_info['isRed']:
            response = "<:ShardRed:1198069899973636137> **Red Shard Today:**\n"\
                       f"Realm: {shard_info['realm']}\n"\
                       f"Map: {shard_info['map']}\n"\
                       f"Reward AC: {shard_info['rewardAC']} <:AscendedCandle:1198069985017331852>\n"\
                       f"Occurences: {occurrences}"
        else:
            response = "<:ShardBlack:1198069944697503894>  **Black Shard Today:**\n"\
                       f"Realm: {shard_info['realm']}\n"\
                       f"Map: {shard_info['map']}\n"\
                       f"Occurences: {occurrences}"
        await interaction.followup.send(response,file=discord.File(map_image_path, filename="map_image.webp"))

    else:
        response = f"**No Shard today!**"

        await interaction.followup.send(response,file=discord.File('public/noShard.gif', filename="map_image.webp"))

@bot.tree.command(name='next_shards')
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
        occurrences = ",".join([f"<t:{int(x.timestamp())}:t>" for x in shard_info['occurrences']])
        formatted_shards.append(
            f"""{config['ShardRed_emoji'] + "Red" if shard_info['isRed'] == 1 else config['ShardBlack_emoji'] + "Black"} shard on {shard_info['date'].strftime('%Y-%m-%d')} in {shard_info['map']} \n \t {config['AscendedCandle_emoji'] if shard_info['isRed']==1 else ''} {occurrences}"""
        )

    # Combine the formatted shards into a single response
    response = "\n\n".join(formatted_shards)

    await interaction.followup.send(response)

# Administrative stuff
@bot.tree.command(
    name="set_daily_quest_channel",
    description="Set up the channel to be cleared daily."
)
@app_commands.checks.has_permissions(administrator=True)
async def set_daily_quest_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    await interaction.response.defer(thinking=True)
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
    your_guild_id = bot.guilds[0].id
    global clear_daily_quest_channel_running
    
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
                    "SELECT channel_id FROM daily_quest_channel"
                )
                channel_result = await cursor.fetchone()
    
            elif not (table_exists and channel_result):
                print("Daily quest channel not set up or table does not exist. Skipping.")
                return
    
    clear_daily_quest_channel_running = True
    
    now = datetime.now(pendulum.timezone('America/Los_Angeles'))  # Set to Pacific Time Zone
    if now.hour == 23 and now.minute == 55 :
        try:
            # Retrieve channel ID from the database based on the guild ID
            async with aioduckdb.connect(db_name) as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute(
                        "SELECT guild_id,channel_id FROM daily_quest_channel WHERE guild_id = ?",
                        (your_guild_id,),
                    )
                    result = await cursor.fetchone()

                    if result:
                        channel_id = result[1]
                        channel = bot.get_channel(channel_id)

                        if channel:
                            await channel.purge(limit=1000)
                            print("Daily quest channel cleared.")
                    else:
                        print("Daily quest channel not set up.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            clear_daily_quest_channel_running = False


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    if not clear_daily_quest_channel_running:
        clear_daily_quest_channel.start(bot)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)

bot.run(sky_bot_token)