import discord
import random #embed field colour
from discord.ext import commands
from discord.ext.commands import Context
from cogs.utils.chat_formatting import pagify
import re

class Mybot:
    def __init__(self, bot):
        """Test commend"""
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, member: discord.Member = None):
        """Display avatar of the user."""
        author = ctx.message.author

        if member is None:
            member = author

        name = str(member)
        if member.avatar:
            avatar = member.avatar_url
            avatar = avatar.replace('webp','png')

        await self.bot.say(avatar)

    @commands.command(pass_context=True, no_pm=True)
    async def emojis(self, ctx: Context, embed=False):
        """Show all emojis available on server."""
        server = ctx.message.server

        if embed:
            emoji_list = [emoji for emoji in server.emojis if not emoji.managed]
            emoji_lists = grouper(25, emoji_list)
            for emoji_list in emoji_lists:
                em = discord.Embed()
                for emoji in emoji_list:
                    if emoji is not None:
                        em.add_field(
                            name=str(emoji), value="`:{}:`".format(emoji.name))
                await self.bot.say(embed=em)
        else:
            out = []
            for emoji in server.emojis:
                # only include in list if not managed by Twitch
                if not emoji.managed:
                    emoji_str = str(emoji)
                    out.append("{} `:{}:`".format(emoji_str, emoji.name))
            for page in pagify("\n".join(out), shorten_by=12):
                await self.bot.say(page)
         
def setup(bot):
    bot.add_cog(Mybot(bot))
