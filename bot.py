import asyncio
import os
import discord 
from discord.ext import commands,tasks
from discord import app_commands
import datetime

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
        name=f"{interaction.user.mention} hugged {member.name} {member.mention}",
        icon_url=interaction.user.avatar)
    await interaction.followup.send(embed = embed1)

clear_daily_quest_channel_running = False
@tasks.loop(minutes=1)
async def clear_daily_quest_channel(bot):
    global clear_daily_quest_channel_running
    clear_daily_quest_channel_running = True
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 0:
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