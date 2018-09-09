import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint

mods = ["400055843787243531"]
rando = randint(1,9)
bypass_list = [""]
chat_filter = ["OOGIEPOOGIENIGGERNOGGER"]
startup_extensions = ["Music"]
bot = commands.Bot(".")

#459871164974628886 - living room
#436290304606339073 - inkopolis plaza
@bot.event
async def on_ready():
    rando
    print("Bot Online")
    print(rando)
    await bot.change_presence(game=discord.Game(name="with Rob's deek"))
    #await bot.send_message(discord.Object(id='459871164974628886'), "Version 1.3.0")
   
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot


@bot.event
async def on_message(message):
    #if message.content.upper().startswith('.REPORT'):
        #if message.author == bot.user:
            #return
        #rob = await bot.get_user_info('400055843787243531')
        #await bot.send_message(rob, "The user {0.author.mention} has reported someone".format(message))
        #henry = await bot.get_user_info('258675615194939392')
        #await bot.send_message(henry, "The user {0.author.mention} has reported someone".format(message))
        #rehan = await bot.get_user_info('310045671094747136')
        #await bot.send_message(rehan, "The user {0.author.mention} has reported someone".format(message))
        #tester = await bot.get_user_info('Tester ID')
        #await bot.send_message(tester, "The user {0.author.mention} has reported someone".format(message))
        
    if message.content.upper().startswith('.HELLO'):
        await bot.send_message(message.channel,"Hello {0.author.mention}! :wave:".format(message))
        
    if message.content.upper().startswith('.HI'):
        await bot.send_message(message.channel,"Hello {0.author.mention}! :wave:".format(message))        
        
    if message.content.upper().startswith('.BYE'):
        await bot.send_message(message.channel,"Hope to see you again soon {0.author.mention}! ;o;".format(message))
        
    if message.content.upper().startswith('.GOODBYE'):
        await bot.send_message(message.channel,"Hope to see you again soon {0.author.mention}! ;o;".format(message))

    if message.content.upper().startswith('.RULES'):
        await bot.send_message(message.channel," #1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. \n #2 Dont advertise. Just dont. Its rude and annoying. \n #3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    if message.content.upper().startswith('.RULE1'):
        await bot.send_message(message.channel,"#1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. ")

    if message.content.upper().startswith('.RULE 1'):
        await bot.send_message(message.channel,"#1 - Be respectul and kind towards others here. Anyone caught harassing or insulting others will receive a warning followed by a kick. ")

    if message.content.upper().startswith('.RULE2'):
        await bot.send_message(message.channel,"#2 Dont advertise. Just dont. Its rude and annoying.")

    if message.content.upper().startswith('.RULE 2'):
        await bot.send_message(message.channel,"#2 Dont advertise. Just dont. Its rude and annoying.")

    if message.content.upper().startswith('.RULE3'):
        await bot.send_message(message.channel,"#3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    if message.content.upper().startswith('.RULE 3'):
        await bot.send_message(message.channel,"#3 Keep all adult and nudity content away from here. Immediate ban for anyone posting obscenities. ")

    #if message.content.upper().startswith('.RULE4'):
        #await bot.send_message(message.channel,"#4 Please do not spam in the server. It is rude and unnecessary.")

    #if message.content.upper().startswith('RULE 4'):
        #await bot.send_message(message.channel,"##4 Please do not spam in the server. It is rude and unnecessary.")

    if message.content.upper().startswith('.YT'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.YOUTUBE'):
        await bot.send_message(message.channel,"https://www.youtube.com/channel/UCel2B-6wZhvQHRAKXmpm1Ew")

    if message.content.upper().startswith('.PING'):
        await bot.send_message(message.channel,"PONG {0.author.mention}".format(message))
        
    #if message.content.upper().startswith('.COMMANDS'):
        await bot.send_message(message.channel," .help: Shows this \n .rules : Displays the rules \n .rules(number of rule): Displays specific rules \n .yt: Link to Eddie's channel! \n .info: Shows info about the bot")
        
    if message.content.upper().startswith('.SPAM'):
        await bot.send_message(message.channel,"Initializing spam...")
        time.sleep(5)
        await bot.send_message(message.channel,"JK {0.author.mention}, please don't spam in the server!".format(message))
        
    #if message.content.upper().startswith(''):
        #await bot.send_message(message.channel,"")
#( ͡° ͜ʖ ͡°)

    await bot.process_commands(message)
    
@bot.command(pass_context=True)
async def info(ctx):
    """Information about the bot"""
    embed=discord.Embed(title="The first Saucefam bot!", description="Functions: Being fun and playing music.", color=0x00FF00)
    embed.set_author(name="WIREDuardo")
    embed.set_footer(text="Created by Robert Jefferson")
    await bot.say(embed=embed)
    print("Information accesed")
    
@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@bot.command(pass_context = True)
async def report(ctx, *args):
    """Usage: .report (@name and cause)"""
    mesg = ' '.join(args)
    
    me = await bot.get_user_info('400055843787243531')
    await bot.send_message(me, "The user {0.author.mention} has reported: {1}".format(ctx.message, mesg))
    
    mac = await bot.get_user_info('414484144115154945')
    await bot.send_message(mac, "The user {0.author.mention} has reported: {1}".format(ctx.message, mesg))
    
    #await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def hello(ctx):
    """Salute the bot!"""

@bot.command(pass_context=True)
async def bye(ctx):
    """Say your goodbyes to the bot..."""
    
@bot.command(pass_context=True)
async def rules(ctx):
    """Shows da rulez."""
    
@bot.command(pass_context=True)
async def rule1(ctx):
    """Shows rule 1."""
    
@bot.command(pass_context=True)
async def rule2(ctx):
    """Shows rule 2."""
    
@bot.command(pass_context=True)
async def rule3(ctx):
    """Shows rule 3."""
    
@bot.command(pass_context=True)
async def yt(ctx):
    """Link to Eddie's YouTube channel."""

@bot.command(pass_context=True)
async def spam(ctx):
    """A naughty command."""
    
@bot.command(pass_context=True)
async def ping(ctx):
    """PONG"""



if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '(): ()'.format(type(e).__name__, e)
print('Failed to load extension ()\n()'.format(extension, exc))

bot.run("NDg4MjIyNzIwMTgyNDUyMjcy.DnZFvQ.oFV6Xq_Nl3QLD13tncwgu_zw8Lg")
