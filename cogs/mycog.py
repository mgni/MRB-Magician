import discord
from discord.ext import commands
#from .utils.chat_formatting import escape_mass_mentions, italics, pagify
#from random import randint
#from random import choice
#from enum import Enum
#from urllib.parse import quote_plus
#import datetime
#import time
#import aiohttp
#import asyncio

class BotEmoji:
    """Emojis available in bot."""

    def __init__(self, bot, mapping=None):
        """Init.
        map: a dictionary mapping a key to to an emoji name.
        """
        self.bot = bot
        self.mapping = mapping

    def name(self, name):
        """Emoji by name."""
        for emoji in self.bot.get_all_emojis():
            if emoji.name == name:
                return '<:{}:{}>'.format(emoji.name, emoji.id)
        return ''

    def named(self, name):
        """Emoji object by name"""
        for emoji in self.bot.get_all_emojis():
            if emoji.name == name:
                return emoji
        return None

    def key(self, key):
        """Chest emojis by api key name or key.
        name is used by this cog.
        key is values returned by the api.
        Use key only if name is not set
        """
        if key in self.mapping:
            name = self.mapping[key]
            return self.name(name)
        return ''

    def key_to_name(self, key):
        """Return emoji name by key."""
        if key in self.mapping:
            return self.mapping[key]
return None
        
class BSData:
    """Brawl Stars Clan management."""

    def __init__(self, bot):
        """Init."""
        self.bot = bot
        self.settings = BSDataSettings(bot)
        self.bot_emoji = BotEmoji(
            bot,
            mapping={
                "Smash & Grab": "icon_smashgrab",
                "Heist": "icon_heist",
                "Bounty": "icon_bounty",
                "Showdown": "icon_showdown",
                "Brawl Ball": "icon_brawlball"
            }
        )
self.sessions = {}
    
    @commands.command(pass_context=True, no_pm=True)
    async def mycom(self, ctx, *, user: discord.Member=None):
        """Shows mycom informations"""
        author = ctx.message.author
        server = ctx.message.server
                
        if not user:
            user = author
            
            def fmt(value, type):
            """Format value by type."""
            if value is None:
                return ''
            if type == int:
            return '{:,}'.format(value)
            
        data = discord.Embed(colour=user.colour)
        data.add_field(name="This is name", value="This is value")
        data.add_field(name="This is name 2", value="This is value 2")
        data.add_field(name="sample", value="This is sample2, [Red, an open source Discord bot](https://discord.gg/red)", inline=False)
        data.add_field(name="Trophies {}".format(self.bot_emoji.name('trophy_bs')), value=fmt(100, int))

        name = str(user)
        if user.avatar:
            avatar = user.avatar_url
            avatar = avatar.replace('webp','png')
            data.set_author(name=name, url=avatar)
            data.set_thumbnail(url=avatar)
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
