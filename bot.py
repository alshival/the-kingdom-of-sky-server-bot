import asyncio
import os
import pytz
import discord 
import random
from discord.ext import commands,tasks
from discord import app_commands
from datetime import datetime,timedelta

discord_bot_token = os.environ.get("fefe_light_token")

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
    await interaction.followup.send(embed = embed1)

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
        response = f"**{'Red' if shard_info['isRed']==1 else 'Black'} Shard Today:**\n"\
                   f"Realm: {shard_info['realm']}\n"\
                   f"Map: {shard_info['map']}\n"\
                   f"Reward AC: {shard_info['rewardAC']}\n"\
                   f"Occurences: {occurrences}"
    else:
        response = f"**No Shard today!**"

    await interaction.followup.send(response,file=discord.File(map_image_path, filename="map_image.webp"))

@bot.tree.command(name='next_shards')
async def next_shards(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    # Get today's date as string
    today_date_str = datetime.utcnow()

    # Get shard info for the next 5 shards
    next_shards_info = shardPredictor.find_next_n_shards(n=5)

    # Format occurrences for each shard
    formatted_shards = []
    for shard_info in next_shards_info:
        occurrences = ",".join([f"<t:{int(x.timestamp())}:t>" for x in shard_info['occurrences']])
        formatted_shards.append(
            f"{'Red' if shard_info['isRed'] == 1 else 'Black'} shard on {shard_info['date'].strftime('%Y-%m-%d')} in {shard_info['map']} \n \t {occurrences}")

    # Combine the formatted shards into a single response
    response = "\n\n".join(formatted_shards)

    await interaction.followup.send(response)

# Administrative stuff
clear_daily_quest_channel_running = False
@tasks.loop(minutes=1)
async def clear_daily_quest_channel(bot):
    global clear_daily_quest_channel_running
    clear_daily_quest_channel_running = True
    now = datetime.now(pytz.timezone('America/Los_Angeles'))  # Set to Pacific Time Zone
    if now.hour == 23 and now.minute == 55:
        try:
            channel_id = 1197511112053239848
            channel = bot.get_channel(channel_id)
    
            if channel:
                await channel.purge(limit=1000)
        except Exception as e:
            print(f"an error occured: {e}")
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

bot.run(discord_bot_token)