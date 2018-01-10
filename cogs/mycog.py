import discord
from discord.ext import commands

class Mybot:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def test(self, ctx, *, user: discord.Member=None):
        """Shows mycom informations"""
        
        author = ctx.message.author
        server = ctx.message.server
  
        if not user:
            user = author
        data = discord.Embed(colour=user.colour)
        data.add_field(name="Name", value="This is value")
        data.add_field(name="Name 2", value="This is value 2")
        data.add_field(name="Sample link", value="This is sample link [Red, an open source Discord bot](https://discord.gg/red)", inline=False)
#       data.set_footer(text="Member #{} | User ID:{}"
#"".format(member_number, user.id)) "

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
            
def setup(bot):
    bot.add_cog(Mycog(bot))
