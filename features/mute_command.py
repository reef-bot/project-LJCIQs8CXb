# mute_command.py

import discord
from discord.ext import commands

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.manage_roles:
            muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
            if not muted_role:
                muted_role = await ctx.guild.create_role(name='Muted')
                for channel in ctx.guild.channels:
                    await channel.set_permissions(muted_role, send_messages=False)
            
            await member.add_roles(muted_role, reason=reason)
            await ctx.send(f'{member.mention} has been muted for: {reason}')
        else:
            await ctx.send('You do not have the necessary permissions to use this command.')

def setup(bot):
    bot.add_cog(MuteCommand(bot))