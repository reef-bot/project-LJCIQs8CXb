# logging_system.py

import discord
from discord.ext import commands

class LoggingSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command. Please check the command and try again.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='welcome')
        if channel:
            await channel.send(f'Welcome {member.mention} to the server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='goodbye')
        if channel:
            await channel.send(f'Goodbye {member.name}. We will miss you!')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = discord.utils.get(message.guild.text_channels, name='logs')
        if channel:
            await channel.send(f'Message deleted by {message.author}: {message.content}')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = discord.utils.get(before.guild.text_channels, name='logs')
        if channel:
            await channel.send(f'Message edited by {before.author}: {before.content} -> {after.content}')

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        channel = discord.utils.get(guild.text_channels, name='logs')
        if channel:
            await channel.send(f'{user.name} has been banned from the server.')

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        channel = discord.utils.get(guild.text_channels, name='logs')
        if channel:
            await channel.send(f'{user.name} has been unbanned from the server.')

def setup(bot):
    bot.add_cog(LoggingSystem(bot))