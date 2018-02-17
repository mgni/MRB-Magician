import discord
import random #embed field colour
import time
import datetime
from discord.ext import commands
from discord.ext.commands import Context

class My_ai:
    def __init__(self, bot):
        """Test commend"""
        self.bot = bot

    async def on_message(self, message):

        greeting = [
            'hi',
            'hello',
            'ဟိုင္း',
            'ဟဲလို',
            'ဟလို'
            ]

        greeting_answer = [
            'ဟိုင္း',
            'ဟိုင္း ေဘဘီ',
            'ဟိုင္း သဲ',
            'ဟဲလို',
            'မဂၤလာပါရွင့္ :blush: ',
            'ဟဲလို ခ်စ္သူ'
            ]

        love_question = [
            'love',
            'ခ်စ္',
            'ေခ်'
            ]

        love_answer = [
            'မသိဘူး သြား လူဇိုး :smile: !!',
            'မေျပာတတ္ဘူး ရွက္တယ္ ခ္ခ္ ..',
            'အေသသတ္သြားလိုက္ >.<',
            'မေတမရွင္ ျဖစ္သြားခ်င္လို႔လားဟင္',
            'သမီးက အသားညိဳတာ မႀကိဳက္ဘူးရွင့္ :joy: ',
            'ဟြန္႔ !! လူလည္ :stuck_out_tongue_winking_eye: ',
            'ဟင့္အင္း သမီးက ငယ္ေသးတယ္ေလ :relaxed: ',
            'ဟင့္အင္း:flushed:  အရမ္းခ်စ္တယ္!!',
            'ေတာ္ပါ ဆက္မေျပာေတာ့ရင္ ဆီလီကြန္အ႐ုပ္မ၀ယ္ေပးမယ္ :yum: ',
            'ဟိဟိ ရင္ခုန္ေအာင္ မလုပ္ရပုေနာ္ :yum: ',
            'သမီး ရွက္တယ္ :stuck_out_tongue_closed_eyes: '
            ]

        if(message.author==self.bot.user):
            return

        message.content = message.content.lower()

        if message.content in greeting:
            answer = random.choice(greeting_answer)
            await self.bot.send_message(message.channel, answer)

        for x in love_question:
            if x in message.content and message.content.endswith(('?','လား')):
                    answer = random.choice(love_answer)
                    await self.bot.send_message(message.channel, answer)
        
        day_name = {
            'sun': 'တနဂၤေႏြ',
            'mon': 'တနဂၤလာ',
            'tue': 'အဂၤါ',
            'wed': 'ဗုဒၶဟူး',
            'thu': 'ၾကာသပေတး',
            'fri': 'ေသာၾကာ',
            'sat': 'စေန'
            }

        day_question = ['ဘာေန','ဘယ္ေန','ဘာရက္','ဘယ္ရက္']
        day_answer = [
            'ဒီေန႔က %sေန႔ေလ',
            'ဒီေန႔က %sေန႔ေပါ့',
            'ဒီေန႔က %sေန႔ထင္တာပဲ',
            'ဒီေန႔က %sေန႔ေလကြယ္'
            ]

        for x in day_question:
            if x in message.content and 'ဒီေန' in message.content:
                day = time.strftime('%a').lower()
                if day in day_name:
                    answer = random.choice(day_answer)  % day_name[day]
                    await self.bot.send_message(message.channel, answer)


    async def on_ready(self):
        await self.bot.change_presence(game=discord.Game(name='say ?help'))

def setup(bot):
    n = My_ai(bot)
    bot.add_cog(n)