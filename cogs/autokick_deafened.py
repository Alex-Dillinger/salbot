from discord.ext import commands
import discord
from discord.utils import get
import logging
import os
automation_logger = logging.getLogger('salc1bot.automated')

class Antideafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.User, state_before, state_after):
        if state_after.self_deaf:
            await member.move_to(None, reason="Anti Deafen")
            automation_logger.info(f"Deafen AutoKick triggered by user {member} ({member.id})")

def setup(bot):
    bot.add_cog(Antideafen(bot))