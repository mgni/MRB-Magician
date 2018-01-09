import discord
from discord.ext import commands
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
import datetime
import time
import aiohttp
import asyncio

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

        
    @commands.command(pass_context=True, no_pm=True)
    async def mycom(self, ctx, *, user: discord.Member=None):
        """Shows mycom informations"""
        author = ctx.message.author
        server = ctx.message.server

        if not user:
            user = author
        data = discord.Embed(description="description", colour=user.colour)
        data.add_field(name="This is name", value="This is value")
        data.add_field(name="This is name 2", value="This is value 2")
#       data.set_footer(text="Member #{} | User ID:{}"
#"".format(member_number, user.id)) "

        if user.avatar_url:
            data.set_author(name=name, url=user.avatar_url)
            data.set_thumbnail(url=user.avatar_url)
        else:
            data.set_author(name=name)

        try:
            await self.bot.say(embed=data)
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission "
"to send this")
            
            
 #       await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
