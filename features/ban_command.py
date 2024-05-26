# ban_command.py

import discord

async def ban_user(ctx, member: discord.Member, reason: str):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for: {reason}')
    except discord.Forbidden:
        await ctx.send('I do not have permission to ban this user.')
    except discord.HTTPException:
        await ctx.send('An error occurred while trying to ban the user. Please try again later.')