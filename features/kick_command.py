# kick_command.py

import discord
from discord.ext import commands

class KickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member == ctx.author:
            await ctx.send("You cannot kick yourself.")
        elif member == self.bot.user:
            await ctx.send("You cannot kick the bot.")
        else:
            try:
                await member.kick(reason=reason)
                await ctx.send(f"{member.mention} has been kicked from the server.")
            except discord.Forbidden:
                await ctx.send("I do not have permission to kick that user.")
            except discord.HTTPException:
                await ctx.send("An error occurred while trying to kick the user.")

def setup(bot):
    bot.add_cog(KickCommand(bot))