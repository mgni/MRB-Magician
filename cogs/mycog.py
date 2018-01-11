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
        data.add_field(name="Emoji", value="This is sample emoji <:bk2:400623664162406411>" + user.name, inline=False)
        
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
            
@commands.command(pass_context=True)
    async def test2(self, ctx):
        """CTX example command"""
        author = ctx.message.author
        description = ("Short little description with a link to "
                       "the [guide](https://github.com/Redjumpman/Jumper-Cogs/wiki/Discord-Coding-Guide)")
        field_name = "Generic Name"
        field_contents = "Example contents for this field"
        footer_text = "Hi. I am a footer text. I look small when displayed."

        embed = discord.Embed(colour=0xFF0000, description=description)  # Can use discord.Colour()
        embed.title = "Cool title for my embed"
        embed.set_author(name=str(author.name), icon_url=author.avatar_url)
        embed.add_field(name=field_name, value=field_contents)  # Can add multiple fields.
        embed.set_footer(text=footer_text)

        await self.bot.say(embed=embed)
            
def setup(bot):
    bot.add_cog(Mybot(bot))
