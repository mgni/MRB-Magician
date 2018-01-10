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
        data.add_field(name="Emoji", value="This is sample emoji <:barbarian:316393732671012864>" + user.name, inline=False)
        
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
            
    @commands.command(pass_context=True, no_pm=True)
    async def clanmsg(self, ctx, *, user: discord.Member=None):
        """Shows clan message for MM Redy Blood clan"""
        
        author = ctx.message.author
        server = ctx.message.server
  
        if not user:
            user = author
            
            mmrb_link = "https://link.clashofclans.com/?action=OpenClanProfile&tag=#82U2R290"
            msgdata_mmrb=("Thi is MMRB Body Text.\nTH9 : 15/15\nTH0 : 35/35\nTH1 : 40/40/20\n")
            member_number=10
            msgdata_footer="Members 30/50 | Win/Loss/Ties: 160/72/0"
            
        data = new discord.Embed(colour=user.colour)
        data.add_field(name="[MM Redy Blood](https://link.clashofclans.com/?action=OpenClanProfile&tag=#82U2R290)", value="", inline=False)
        data.add_field(name="[Goto Clan](https://link.clashofclans.com/?action=OpenClanProfile&tag=#82U2R290)", value=msgdata_mmrb, inline=False)
        data.add_field(name="<:bk2:400623664162406411>Leader:", value="LeaderName")
        data.add_field(name="TH levels accepted:", value="<:th9:400623665005330442> <:th10:400623664195829770> <:th11:400623664824844288>")
        data.add_field(name="Allowed in war:", value="<:th9:400623665005330442> = <:bk:400623663809822730> <:aq:400623663952560128>\n"
                       "<:th10:400623664195829770> = <:bk:400623663809822730> <:aq:400623663952560128>\n"
                       "<:th11:400623664824844288> = <:bk:400623663809822730> <:aq:400623663952560128> <:gw:400623663998697493>")
        
        data.set_footer(msgdata_footer)

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
    bot.add_cog(Mybot(bot))
