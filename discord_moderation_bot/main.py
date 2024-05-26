# main.py

import discord
from discord.ext import commands
from features.warning_system import WarningSystem
from features.logging_system import LoggingSystem
from features.mute_command import MuteCommand
from features.kick_command import KickCommand
from features.ban_command import BanCommand

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready to moderate!')

# Initialize features
warning_system = WarningSystem()
logging_system = LoggingSystem()
mute_command = MuteCommand()
kick_command = KickCommand()
ban_command = BanCommand()

# Warning command
@client.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    await warning_system.warn(ctx, member, reason)

# Mute command
@client.command()
async def mute(ctx, member: discord.Member, *, duration=None):
    await mute_command.mute(ctx, member, duration)

# Kick command
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await kick_command.kick(ctx, member, reason)

# Ban command
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ban_command.ban(ctx, member, reason)

# Run the bot
client.run('your_token_here')