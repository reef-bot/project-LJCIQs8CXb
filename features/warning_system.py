warning_system.py

# Import necessary modules
import discord
from discord.ext import commands

# Define the warning system cog
class WarningSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to issue a warning to a user
    @commands.command(name='warn')
    async def warn(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            await ctx.send("Please provide a reason for the warning.")
            return

        # Implement logic to issue a warning to the user
        # You can store warnings in a database or file for future reference
        # For now, just send a warning message to the user
        await user.send(f"You have been warned for: {reason}")
        await ctx.send(f"{user.mention} has been warned for: {reason}")

# Setup function to add the cog to the bot
def setup(bot):
    bot.add_cog(WarningSystem(bot))